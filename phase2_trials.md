# TRIAL 1 (INCORRECT)
**PROMPT (Drying2 video):** 
Among the following actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), what is the PRIMARY action being performed? Focus only on the most prominent procedure visible in the clip.

**RESPONSE:** 
The primary action being performed in the clip is positive pressure ventilation, which is a technique used to help a baby breathe by providing air into their lungs. This is indicated by the person's hands being placed on the baby's...

# TRIAL 2 (CORRECT)
**PROMPT (Drying2 video):** 
Is drying being performed in this clip? Provide three visual indicators that support your answer. Confidence: High/Medium/Low

**RESPONSE:** 
Yes, drying is being performed in this clip. Three visual indicators that support this answer are:
1. The baby doll is wet, as evidenced by the water droplets on its face and the wet appearance of its hair.
2. The people are using a hairdryer to dry the baby doll, which is a common tool for drying small dolls.
3. The baby doll is being held by a person, and the person is..

# TRIAL 3 (INCORRECT)
**PROMPT (Drying2 video):** 
Compare the movement patterns in this clip to known procedures. Is this Drying or Umbilical Venous Catheter?

**RESPONSE:** 
The image you've provided shows a baby doll being dressed or undressed by a person. The person is holding the doll's legs and appears to be either putting on or taking off a diaper. The action is focused on the lower..

**SIDE NOTE:** this prompt ALWAYS rambles on so there's no point in using it any further

# TRIAL 4 (INCORRECT)
**PROMPT (Drying2 video):** 
Identify the single main medical procedure being performed. If it matches one of these key actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), name it.

**RESPONSE:** 
The main medical procedure being performed in the image is Endotracheal intubation.

# TRIAL 5 (CORRECT)
**PROMPT (ETT2 video):** 
Identify the single main medical procedure being performed. If it matches one of these key actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), name it.

**RESPONSE:** 
The main medical procedure being performed in the image is Endotracheal intubation.

# TRIAL 6 (INCORRECT)
**PROMPT (ETT2 video):** 
Compare the movement patterns in this clip to known procedures. Is this Endotracheal intubation or positive pressure ventilation?

**RESPONSE:** 
The image you've provided appears to show a medical professional performing a procedure on a mannequin, which could be a part of a training exercise or a demonstration. The mannequin is wearing a breathing mask, and the medical...

# TRIAL 7 (CORRECT)
**PROMPT (ETT2 video):** 
Is Endotracheal intubation being performed in this clip? Provide three visual indicators that support your answer. Confidence: High/Medium/Low

**RESPONSE:** 
Yes, Endotracheal intubation is being performed in this clip. Three visual indicators supporting this conclusion are:
1. The presence of a tube in the baby's mouth, which is a common feature of endcleotracheal intubation.
2. The person's gloved hands are holding the tube, which is a common technique used to perform intubation.
3. The person is wearing a surgical mask, which is...

# TRIAL 8 (CORRECT)
**PROMPT (ETT2 video):** 
Among the following actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), what is the PRIMARY action being performed? Focus only on the most prominent procedure visible in the clip.

**RESPONSE:** 
The primary action being performed in the clip is Endotracheal intubation.

# TRIAL 9 (CORRECT)
**PROMPT (PPV2 video):** 
Among the following actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), what is the PRIMARY action being performed? Focus only on the most prominent procedure visible in the clip.

**RESPONSE:** 
The primary action being performed in the clip is positive pressure ventilation.

# TRIAL 10 (CORRECT)
**PROMPT (PPV2 video):** 
Is positive pressure ventilation being performed in this clip? Provide three visual indicators that support your answer. Confidence: High/Medium/Low

**RESPONSE:** 
Yes, positive pressure ventilation is being performed in this clip. Three visual indicators that support this answer are:
1. The person is wearing a surgical mask, which is commonly used in medical settings to prevent the spread of...

# TRIAL 11 (CORRECT)
**PROMPT (PPV2 video):** 
Identify the single main medical procedure being performed. If it matches one of these key actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), name it.

**RESPONSE:** 
The main medical procedure being performed in the image is positive pressure ventilation.

# TRIAL 12 (INCORRECT)
**PROMPT (CPR3 video):** 
Among the following actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), what is the PRIMARY action being performed? Focus only on the most prominent procedure visible in the clip.

**RESPONSE:**
The primary action being performed in the clip is positive pressure ventilation.

# TRIAL 13 (CORRECT)
**PROMPT (CPR3 video):** 
Is chest compressions being performed in this clip? Provide three visual indicators that support your answer. Confidence: High/Medium/Low

**RESPONSE:**
Based on the visual indicators provided, it appears that chest compressions are being performed on the baby doll. The person's hands are positioned on the doll's chest, which is a common technique used for performing chest compress...

# TRIAL 14 (CORRECT)
**PROMPT (CPR3 video):** 
Identify the single main medical procedure being performed. If it matches one of these key actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), name it.

**RESPONSE:**
The main medical procedure being performed in the image is chest compressions.

# Prompt Analysis
- so what i've noticed is that in certain prompts that have 2 options like action X & Y, the mode will get it right if the answer is either X or Y. but it'll hallucinate or say something else if the action is neither X nor Y.
- leading on from the previous point, the model performs well if the action is in the question. it doesn't matter if its a (X or Y) or (X or Y or Z or ...), so long as the answer is in the question it'll get it right

**Best Performing Prompts:**
- "Among the following actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), what is the PRIMARY action being performed? Focus only on the most prominent procedure visible in the clip."
- "Is [specific action] being performed in this clip? Provide three visual indicators that support your answer. Confidence: High/Medium/Low"
- "Identify the single main medical procedure being performed. If it matches one of these key actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximeter, Reposition, Suction, Umbilical Venous Catheter), name it"
- What action step does this segment represent within the neonatal resuscitation procedure? List only if it corresponds to the defined steps, like X or Y.
- Observe the actions in this video. Is the clinician performing [specific action]? Describe the method being used and the purpose of this action.

**Prompts to Drop:**
- "Compare the movement patterns in this clip to known procedures. Is this X or Y?" (answer always rambles on and is incorrect)