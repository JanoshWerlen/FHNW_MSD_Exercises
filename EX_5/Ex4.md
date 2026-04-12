# Evaluation of the TMS (Training Management System) SRS

## 1. Who created the final version?
The final version (v1.0) was created by:
- Osamah Yacoub  
- Ahmad Arrabi  

---

## 2. What is the intended use?
The SRS document is intended to:
- Capture the complete software requirements  
- Serve as a basis for design, development, and testing  
- Be approved by the client  
- Provide a shared understanding between stakeholders and developers  

---

## 3. Who are the intended users?
The system is designed for the following user groups:
- System Administrator  
- PMU Administrator  
- TP Administrator  
- Training Coordinator (TC)  
- Government of Jordan (GoJ) Employees  

---

## 4. What is the standard environment?
Key characteristics of the environment:
- Web-based application (Internet/Intranet)  
- Supported browser: Microsoft Internet Explorer 5.0 or above  
- Screen resolution: 800x600  
- Languages: English and Arabic  
- Runtime environment provided by the client (hardware, software, network)  

---

## 5. Functional Requirement Evaluation

### Example: FR01 – Course/Test Maintenance  
**Description:** Add, update, and delete courses or tests  

| Criterion     | Evaluation | Explanation |
|--------------|------------|-------------|
| Complete     | ❌ No       | Missing details such as data fields, validation rules, constraints |
| Accurate     | ✔️ Yes      | Correctly describes intended CRUD functionality |
| Unambiguous  | ❌ No       | Terms and scope are not precisely defined |
| Traceable    | ✔️ Yes      | Clearly identified with ID (FR01) |
| Testable     | ⚠️ Partial  | Basic functionality testable, but lacks acceptance criteria |

---

## 6. Is there a requirement regarding data security?
✔️ Yes  

Security-related aspects include:
- User authentication via login (User ID and Password)  
- Role-based access control (different permissions per user group)  

⚠️ However, the requirements are:
- High-level  
- Lacking technical details (e.g., encryption, password policies)  

---

## 7. Is there a requirement on how the software should be designed?
✔️ Yes  

Design constraints include:
- Use of a 3-tier architecture  
- XML support for interoperability with future systems  

These define the high-level architectural approach of the system.  

---