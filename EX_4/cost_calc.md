# Project Planning – Estimation using Widget Points & Function Points

## 1. Widget Point Analysis

### Input Widgets
- Sensor Select Box (ComboBox) → 1  
- Add Button → 1  
- Remove Button → 1  
- Start/Stop Button → 1  

**Total Input Widgets: 4**

---

### Describing Widgets
- App Title → 1  
- Label for Sensor Selection → 1  
- Label for Selected Sensors List → 1  

**Total Describing Widgets: 3**

---

### Composite Widgets
- Selected Sensors List (List/Table) → 1  

**Total Composite Widgets: 1**

---

### Menu Widgets
- None → 0  

---

### ✅ Total Widget Points

\[
WP = 4 + 3 + 1 + 0 = 8
\]

---

## 2. Function Point Calculation

Using the formula:

FP = 2 x WP


FP = 2 x 8 = 16


---

## 3. LOC Estimation

Using Java/mobile approximation:

- 1 Function Point ≈ 53 LOC  

LOC = 16 x 53 = 848

**Estimated LOC: ~850**

---

## 4. Effort Estimation (COCOMO)

Assumptions:
- Project Type: Organic (simple)
- KDL = 0.85 (850 LOC)

Formula:

E = 3.2 x (KDL)^1.05


E = 3.2 x (0.85)^1.05 = approx 2.7 person-months


---

## Adjustment Factors

complexity of product - very low (0.7)

2.7 x 0.7 = 1.9

E = 1.9 

## 5. Project Duration

D = 2.5 x E^0.38

D = 2.5 x (1.9)^0.38 = ca. 3.2  months

---

## 6. Team Size


P = {E}/{D}


P = {1.9}/{3.2} = ca. 0.6


**Estimated Team Size: 0.6 FTE Developer**

---

## 7. Cost Estimation

CHF 10'000.- per Month

1.9 * 10'000 = CHF 19'000

---

## 8. Final Summary

| Metric | Value |
|------|------|
| Widget Points | 8 |
| Function Points | 16 |
| LOC | ~850 |
| Effort | ~1.9 Person-Months |
| Duration | ~3.2 Months |
| Team Size | ~1 Developer |
| Cost | CHF 19k |
