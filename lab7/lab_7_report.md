# Lab 7: Fuzzing for Input Validation Bugs

**Name:** Akula Pragnya  
**SRN:** PES1UG24AM096  
**Repository:** L6_L7_96_airline_baggage  

---

### 1. Baseline & Fuzzing Failure Analysis
* **Test File:** `test_airline_baggage.py`
* **Fuzzing Tool:** Hypothesis framework with `pytest`
* **Initial Test Result:** 3 Failed (Unhandled Exceptions)
* **Analysis:** Fuzz testing with property-based input strategies (`st.text() | st.none() | st.integers() | st.floats() | st.lists(st.text())`) exposed critical input validation bugs in `parse_booking`, `total_weight`, and `tag_label`. The functions crashed when presented with empty strings (`''`) and `None` values, raising unhandled `ValueError`, `AttributeError`, and `IndexError` exceptions.

---

### 2. Code Hardening & Verification Analysis
* **Application File:** `airline_baggage.py`
* **Hardened Test Result:** 3 Passed (100% Pass Rate across generated inputs)
* **Execution Time:** 0.95 seconds
* **Analysis:** Applied defensive programming techniques including explicit type guards (`isinstance(s, str)`), length boundary verification, numeric parsing error trapping (`try-except`), and non-negative value constraints. Re-running Hypothesis fuzz tests confirmed that all functions now handle arbitrary malformed and edge-case inputs gracefully without crashing.

---

### 3. Conclusion
Fuzz testing using Hypothesis effectively uncovered edge-case input validation bugs that standard manual testing missed. By implementing robust type guards and defensive error handling, the application script was successfully hardened against all malformed inputs, achieving a 100% pass rate across property-based fuzz test suites.

---

### 4. Evidence
* **Baseline Output Screenshot:** `screenshots/step2_interactive_run.png`
* **Hypothesis Failure Screenshots:** `screenshots/step4_fuzz_failures.png`
* **Hardened Verification Screenshot:** `screenshots/step6_fuzz_passing.png`