# Medical Procedure Prompt Analysis

## Overview
Analysis of prompt performance for medical procedure identification in video clips, including performance metrics and recommended prompts based on empirical results.

## Accuracy Analysis

### Overall Accuracy by Prompt Type

#### Prompt Type 1: Yes/No with 3 Visual Indicators
- **Format**: Question asking if specific procedure is being performed with requirement for 3 visual indicators
- **Accuracy**: 8/13 correct (61.5%)
- **Characteristics**: Detailed, structured response with visual evidence required
- **Strengths**: Forces justification and specific observation

#### Prompt Type 2: Single Main Procedure Identification
- **Format**: Direct identification of main procedure from list
- **Accuracy**: 6/13 correct (46.2%)
- **Characteristics**: Direct, single-answer focused
- **Weaknesses**: Lacks requirement for justification

#### Prompt Type 3: Select PRIMARY Action from List
- **Format**: Multiple choice selection of primary action
- **Accuracy**: 3/13 correct (23.1%)
- **Characteristics**: Multiple choice with focus on primary action
- **Weaknesses**: Too open-ended, lacks structured analysis

### Procedure-Specific Accuracy

| Procedure | Success Rate | Accuracy |
|-----------|--------------|-----------|
| PPV | 3/4 | 75% |
| ETT | 3/3 | 100% |
| CPR | 1/3 | 33.3% |
| Drying | 1/2 | 50% |
| Pulse Oximetry | 1/2 | 50% |
| Suction | 1/1 | 100% |
| Repositioning | 1/1 | 100% |

## Best Performing Elements

### Effective Features
1. Requirement for specific visual indicators
2. Binary (yes/no) initial questions
3. Structured response requirements
4. Confidence level ratings
5. Direct identification tasks

### Problematic Elements
1. Open-ended selection from multiple options
2. Lack of visual evidence requirements
3. Missing confidence ratings
4. Unstructured response formats

## Recommended Improved Prompts

### Five Best Suggested Prompts

1. "Is [specific procedure] being performed in this clip? Provide exactly three visual indicators supporting your answer. State confidence level (High/Medium/Low)."

2. "List three pieces of medical equipment visible in use. Based only on equipment usage, which procedure is being performed? Provide three visual confirmations."

3. "What is the primary location of healthcare provider's hands? Based on hand placement and movement, which ONE procedure from [list] is being performed? Provide three visual indicators."

4. "Observe for 3 seconds. From [procedure list], eliminate procedures that cannot be occurring based on visible evidence. Name the procedure being performed with three specific visual indicators."

5. "What medical procedure matches ALL of these criteria: Current hand position, Equipment in use, Patient positioning? Provide three visual confirmations and confidence level."