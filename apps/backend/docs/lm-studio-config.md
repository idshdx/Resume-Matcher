# LM Studio Configuration Guide for Resume Matcher

This guide provides the system prompts and JSON schemas required to configure LM Studio's structured output for the Resume Matcher's AI features.

### System Prompt General
```text
You are an expert resume analyst, writer and editor. Output only valid JSON.

You must respond with valid JSON only. No explanations, no markdown.
```

## 1. Resume Tailoring & Improvement
**Routes:** `/builder`, `/tailor`
**Feature:** AI Improvement / Tailoring to Job Description

### System Prompt
```text
You are an expert resume editor. Output only valid JSON.

You must respond with valid JSON only. No explanations, no markdown.
```

### JSON Schema (ResumeData)
```json
{
  "title": "ResumeData",
  "type": "object",
  "properties": {
    "personalInfo": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "title": { "type": "string" },
        "email": { "type": "string" },
        "phone": { "type": "string" },
        "location": { "type": "string" },
        "website": { "type": ["string", "null"] },
        "linkedin": { "type": ["string", "null"] },
        "github": { "type": ["string", "null"] }
      }
    },
    "summary": { "type": "string" },
    "workExperience": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "integer" },
          "title": { "type": "string" },
          "company": { "type": "string" },
          "location": { "type": ["string", "null"] },
          "years": { "type": "string" },
          "description": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    "education": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "integer" },
          "institution": { "type": "string" },
          "degree": { "type": "string" },
          "years": { "type": "string" },
          "description": { "type": ["string", "null"] }
        }
      }
    },
    "personalProjects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "integer" },
          "name": { "type": "string" },
          "role": { "type": "string" },
          "years": { "type": "string" },
          "description": { "type": "array", "items": { "type": "string" } }
        }
      }
    },
    "additional": {
      "type": "object",
      "properties": {
        "technicalSkills": { "type": "array", "items": { "type": "string" } },
        "languages": { "type": "array", "items": { "type": "string" } },
        "certificationsTraining": { "type": "array", "items": { "type": "string" } },
        "awards": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

---

## 2. Resume Enrichment Analysis
**Routes:** `/resumes/[id]`
**Feature:** AI Analysis of resume weaknesses and question generation.

### System Prompt
```text
You are a professional resume analyst. You must respond with valid JSON only. No explanations, no markdown.
```

### JSON Schema (AnalysisResponse)
```json
{
  "title": "AnalysisResponse",
  "type": "object",
  "properties": {
    "items_to_enrich": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "item_id": { "type": "string" },
          "item_type": { "type": "string" },
          "title": { "type": "string" },
          "subtitle": { "type": ["string", "null"] },
          "current_description": { "type": "array", "items": { "type": "string" } },
          "weakness_reason": { "type": "string" }
        },
        "required": ["item_id", "item_type", "title", "weakness_reason"]
      }
    },
    "questions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "question_id": { "type": "string" },
          "item_id": { "type": "string" },
          "question": { "type": "string" },
          "placeholder": { "type": "string" }
        },
        "required": ["question_id", "item_id", "question"]
      }
    },
    "analysis_summary": { "type": ["string", "null"] }
  }
}
```

---

## 3. AI Item & Skills Regeneration
**Routes:** `/builder`
**Feature:** Regenerating specific sections based on feedback.

### System Prompt
```text
You are a professional resume writer. You must respond with valid JSON only. No explanations, no markdown.
```

### JSON Schema (Item Regeneration)
```json
{
  "title": "RegenerateItemResponse",
  "type": "object",
  "properties": {
    "new_bullets": {
      "type": "array",
      "items": { "type": "string" }
    },
    "change_summary": { "type": "string" }
  },
  "required": ["new_bullets", "change_summary"]
}
```

### JSON Schema (Skills Regeneration)
```json
{
  "title": "RegenerateSkillsResponse",
  "type": "object",
  "properties": {
    "new_skills": {
      "type": "array",
      "items": { "type": "string" }
    },
    "change_summary": { "type": "string" }
  },
  "required": ["new_skills", "change_summary"]
}
```

---

## 4. AI Description Enhancement
**Routes:** `/resumes/[id]`
**Feature:** Adding new bullet points based on candidate answers.

### System Prompt
```text
You are a professional resume writer. You must respond with valid JSON only. No explanations, no markdown.
```

### JSON Schema (EnhanceDescriptionResponse)
```json
{
  "title": "EnhanceDescriptionResponse",
  "type": "object",
  "properties": {
    "additional_bullets": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["additional_bullets"]
}
```
