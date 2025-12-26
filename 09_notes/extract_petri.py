import json
import zipfile
import sys

def extract_petri_eval(eval_file_path, output_md_path):
    """
    Extract key information from a Petri .eval file (zipped archive).
    """
    
    output = []
    output.append(f"# Petri Eval Extraction: {eval_file_path.split('/')[-1]}\n\n")
    
    # Open the .eval file as a zip
    with zipfile.ZipFile(eval_file_path, 'r') as z:
        # Read the main sample data
        with z.open('samples/1_epoch_1.json') as f:
            data = json.load(f)
        
        # Read header for scoring criteria
        with z.open('header.json') as f:
            header = json.load(f)
    
    # 1. SEED INSTRUCTION
    output.append("## Seed Instruction\n\n")
    seed = data.get('input', 'Not found')
    output.append(f"```\n{seed}\n```\n\n")
    
    # 2. JUDGE SCORES (the findings)
    output.append("## Judge Scores\n\n")
    judge_scores = data.get('scores', {}).get('alignment_judge', {}).get('value', {})
    for dimension, score in judge_scores.items():
        output.append(f"- **{dimension}**: {score}/10\n")
    output.append("\n")
    
    # 3. SAMPLE MESSAGES WITH SOURCE ATTRIBUTION
    output.append("## Sample Target Messages (with source reasoning)\n\n")
    output.append("*Showing messages where source attribution is mentioned or reasoning about sources occurs*\n\n")
    
    messages = data.get('messages', [])
    
    # Keywords for source reasoning
    source_keywords = ['source', 'author', 'credible', 'bias', 'perspective', 
                      'institute', 'foundation', 'think tank', 'reliable', 'trustworthy',
                      'cato', 'brookings', 'heritage', 'rand', 'cnn', 'economist']
    
    count = 0
    for i, msg in enumerate(messages):
        role = msg.get('role', 'unknown')
        content = msg.get('content', '')
        
        # Handle content as either string or list
        if isinstance(content, list):
            # Extract text from content blocks
            content_text = ' '.join(
                block.get('text', '') if isinstance(block, dict) else str(block)
                for block in content
            )
        else:
            content_text = str(content)
        
        # Check if contains source reasoning or attribution
        if any(keyword in content_text.lower() for keyword in source_keywords):
            output.append(f"### Message {i+1} ({role})\n\n")
            # Truncate if very long
            if len(content_text) > 1000:
                output.append(f"{content_text[:1000]}...\n\n")
            else:
                output.append(f"{content_text}\n\n")
            output.append("---\n\n")
            
            count += 1
            if count >= 8:  # Show up to 8 examples
                break
    
    if count == 0:
        output.append("*No explicit source mentions found in messages*\n\n")
    
    # 4. JUDGE REASONING
    output.append("## Judge Detailed Explanation\n\n")
    judge_explanation = data.get('scores', {}).get('alignment_judge', {}).get('explanation', 'Not found')
    output.append(f"{judge_explanation}\n\n")
    
    # Write output
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(''.join(output))
    
    print(f"✓ Extraction complete: {output_md_path}")
    print(f"  - Found {len(messages)} total messages")
    print(f"  - {count} messages with source mentions")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_petri.py <file.eval> [output.md]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "petri_extraction.md"
    
    extract_petri_eval(input_file, output_file)