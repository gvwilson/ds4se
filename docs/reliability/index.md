# Coding Schemes and Inter-Rater Reliability

## Learning Goals

-   Explain why [%g inter_rater_reliability "inter-rater reliability" %] is necessary for qualitative research
-   Compute [%g cohens_kappa "Cohen's kappa" %] and interpret the result using standard thresholds
-   Write a [%g codebook "codebook" %] that enables independent replication
-   Identify common mistakes in reporting inter-rater reliability

---

-   If only one person codes the data, the results reflect that person's interpretation
    -   A second independent coder is the most common check against this
    -   "Independent" means the two coders do not discuss items before recording their codes
    -   After coding independently, you measure how often they agreed

-   Percent agreement is not enough
    -   If two coders classify everything as "bug fix" they agree 100% of the time
    -   But they would also agree 100% of the time by random chance if the only category were "bug fix"
    -   You need a measure that corrects for how much agreement chance alone would produce

-   Cohen's kappa corrects for chance agreement
    -   kappa = (observed agreement - expected agreement) / (1 - expected agreement)
    -   Expected agreement is what two coders would achieve if each coded items independently at random,
        according to the frequency with which each uses each category
    -   kappa < 0.4: poor agreement; 0.4 to 0.6: moderate; 0.6 to 0.8: substantial; above 0.8: near-perfect
    -   These thresholds are conventions, not laws — report the number and let readers judge

-   Krippendorff's alpha generalizes kappa to more than two raters and to ordinal or continuous codes
    -   Use it when you have three or more coders or when your codes have a natural order

-   Wang et al. used card sorting to classify reasons why bugs go unfixed in Mozilla, Eclipse, and
    Apache OpenOffice [%b Wang2020a %]
    -   Two researchers sorted the same cards independently
    -   Disagreements were discussed until consensus; unresolvable cases were noted as limitations
    -   They report kappa for each classification pass, showing improvement across passes

-   A codebook makes your coding scheme replicable
    -   Each code gets a name, a one or two sentence definition, at least one example of text that
        fits, and at least one example of text that does not fit
    -   A good codebook lets a researcher who was not involved in the original study reach the same
        conclusions on the same data
    -   Writing a codebook forces you to articulate distinctions you might otherwise leave implicit

-   Handling disagreements between coders
    -   Discuss until consensus: the most common approach; produces a single agreed coding
    -   Add a "borderline" category for cases where no consensus is possible
    -   Bring in a third coder as a tiebreaker
    -   Report unresolved disagreements as a limitation; this is underused and underappreciated

-   The most common mistake: coding together, not independently
    -   Two coders discuss each item before recording their labels
    -   They then report high agreement as evidence of reliability
    -   This is circular: they agreed because they talked, not because the codebook is clear
    -   Independent coding must happen before any discussion

-   The code below computes percent agreement and Cohen's kappa for two lists of labels

[%inc kappa.py %]

-   Running this on the example in the file produces:
    -   Percent agreement: 70.0%
    -   Cohen's kappa: 0.534
    -   Interpretation: moderate
    -   One code boundary is ambiguous; a revision to the codebook is needed

## Check Understanding

<details markdown="1">
<summary markdown="1">Why is percent agreement not sufficient for measuring inter-rater reliability? What does Cohen's kappa add?</summary>

Percent agreement does not account for agreement that would occur by chance given the distribution
of codes in the data. If one category dominates (for example, 90% of items are "not relevant"),
two coders independently guessing at random would still agree 82% of the time just from base rates.
Cohen's kappa subtracts the expected chance agreement from the observed agreement before dividing,
so a high kappa means the coders are genuinely agreeing on meaning rather than accidentally choosing
the same dominant category.

</details>

<details markdown="1">
<summary markdown="1">What is wrong with the following code, and how do you fix it?

```python
# Two coders discuss each item together and then record their "independent" codes
coder_a = [code_item(item, discussion=True) for item in items]
coder_b = [code_item(item, discussion=True) for item in items]
kappa = cohen_kappa(coder_a, coder_b)
```
</summary>

The coders discussed each item before recording their codes, so the codes are not independent.
Any agreement reflects shared discussion rather than the clarity of the codebook. Computing kappa
on codes that were negotiated before recording is meaningless as a reliability measure because it
does not tell you whether a third coder, working alone with only the codebook, would reach the
same conclusions. The fix is to have each coder work through all items independently, recording
their codes without any communication, before comparing results and computing kappa. Only after
computing kappa should they discuss disagreements to reach consensus.

</details>

<details markdown="1">
<summary markdown="1">Wang et al. report kappa for each classification pass of their card sorting, and kappa improves between passes. Why might kappa improve beyond the coders simply practicing?</summary>

Each time the coders compare results and discuss disagreements, they sharpen the codebook implicitly.
After the first pass, they discover which distinctions were ambiguous and refine how they think about
those boundaries. The second pass is therefore performed with an improved shared understanding of the
categories, even if the written codebook has not changed. In addition, the act of explaining your
reasoning to another coder forces you to make tacit distinctions explicit, which helps both coders
apply the scheme more consistently on the next pass.

</details>

<details markdown="1">
<summary markdown="1">A researcher codes 200 issue comments solo and reports "95% internal consistency." What is wrong with this claim?</summary>

Internal consistency (often measured by Cronbach's alpha or similar) is a property of survey scales,
not of qualitative coding. Applying it to coding makes no methodological sense. More importantly,
one person coding alone cannot produce a reliability estimate at all — reliability requires
independent coders. What the researcher should have done is recruited a second coder, provided them
with a codebook, had them code a sample independently, and then computed Cohen's kappa. A solo coder
producing a high "consistency" number is measuring something, but not inter-rater reliability.

</details>

## Exercises

<div class="exercise" markdown="1">
### Computing kappa on your own codes

Return to the ten Stack Overflow comments you coded in Lesson 20. Give the same comments to a
partner, along with the codebook you wrote, but do not discuss the comments before your partner
codes them. After both of you have recorded your codes independently, compute percent agreement and
Cohen's kappa using the `kappa.py` script. If kappa is below 0.6, identify the one code definition
that caused the most disagreements and rewrite it so that it includes an explicit example and a
non-example.
</div>

<div class="exercise" markdown="1">
### Writing and applying a codebook

Write a three-code codebook for classifying pull request review comments as "requesting a change,"
"asking a question," or "approving." For each code, write a definition, one example of a real
comment that fits, and one example of a real comment that does not fit. Apply the codebook to ten
review comments from any public GitHub repository, then give the codebook and the same ten comments
to a partner and have them code independently. Compute Cohen's kappa and note which pair of codes
caused the most disagreements.
</div>

<div class="exercise" markdown="1">
### Explaining kappa improvement across passes

Wang et al. report kappa values for each coding pass of their card sorting study and observe
improvement between passes. Write two explanations for why kappa might improve between the first
and second pass that go beyond simply saying "we practiced." For each explanation, write one
sentence describing what a researcher could do to take advantage of that mechanism deliberately
rather than just hoping improvement occurs.
</div>

<div class="exercise" markdown="1">
### Critiquing a solo coding claim

A researcher codes 200 GitHub issue comments alone and reports 95% internal consistency as evidence
that their coding scheme is reliable. Write three sentences explaining what is wrong with this
claim. In a fourth sentence, describe exactly what the researcher should have done instead, naming
the measure they should have computed and the minimum acceptable value by the conventions in this
lesson.
</div>

<div class="exercise" markdown="1">
### Computing expected agreement by hand

Consider a two-category coding scheme where coder A assigns 60% of items to category 1 and 40%
to category 2, and coder B assigns 70% to category 1 and 30% to category 2. Compute the expected
agreement by chance. Then compute the Cohen's kappa you would achieve if the observed agreement
were 80%. Show your arithmetic at each step. State whether the resulting kappa meets the threshold
for "substantial" agreement by the conventions in this lesson, and write one sentence interpreting
what that means for a paper reporting this result.
</div>
