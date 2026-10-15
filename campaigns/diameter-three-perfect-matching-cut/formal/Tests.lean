import Challenge
open DiameterThreePerfectMatchingCut
example : legalSource ⟨5, [(0,1),(1,2),(2,3),(3,4)]⟩ = true := by native_decide
example : legalTarget ⟨5, [(0,1),(1,2),(2,3),(3,4)]⟩ = false := by native_decide
