# Computational Based Comparison of COVID-19 Vaccine Sentiment Between Occupational Groups on Reddit in 2021

---

## Abstract

**Background:** The success of the global COVID-19 vaccination campaign was contingent not only on supply and logistics but also on public acceptance, which was heavily influenced by online discourse. Understanding how different societal groups discuss and perceive vaccines is critical for effective public health communication.

**Objective:** This study aimed to analyze and compare sentiment towards COVID-19 vaccines between blue-collar and white-collar occupational communities on the social media platform Reddit during the peak of the vaccine rollout in 2021.

**Methods:** A purposive sampling strategy was used to select 17 profession-specific subreddits, categorized as either "blue-collar" or "white-collar." Using the Python Reddit API Wrapper (PRAW), a total of 846 relevant posts and comments containing keywords such as "vaccine," "pfizer," or "moderna" were collected from January 1, 2021, to December 31, 2021. Sentiment for each text item was classified as positive, neutral, or negative using Google's Gemini 2.5 Flash large language model, with model temperature and thinking budget set to 0 for deterministic output. These classifications were converted to a numeric scale (-1 for negative, 0 for neutral, 1 for positive). An independent samples t-test was used to compare mean sentiment scores between the two categories. A supplementary qualitative analysis was performed to explore thematic differences in discourse.

**Results:** The final dataset consisted of 363 items from blue-collar subreddits and 483 from white-collar subreddits. Overall, the mean sentiment score in the white-collar category (M = -0.24, 95% CI [-0.31, -0.17]) was significantly more negative than the near-neutral sentiment in the blue-collar category (M = -0.01, 95% CI [-0.10, 0.09]), a statistically significant difference (p < .001). Proportional analysis revealed that blue-collar communities had a much higher percentage of positive comments (39.9%) than white-collar communities (19.3%). However, analysis of individual subreddits revealed significant intra-category heterogeneity, challenging the meaning of the overall average.

**Conclusion:** This study reveals a significant difference in COVID-19 vaccine sentiment between online blue-collar and white-collar communities. However, the "illusion of the average" masks profound variations within these broad categories. Public health messaging must move beyond simplistic demographic targeting and instead be tailored to the specific values, concerns, and discursive frameworks of distinct occupational groups to effectively address vaccine hesitancy.

---

## 1. Introduction

The COVID-19 pandemic necessitated unprecedented vaccination efforts, but public reception was deeply fragmented. This fragmentation was influenced by a complex interplay of socioeconomic factors, political ideology, and an evolving information landscape characterized by an "infodemic" on social media (Zarocostas, 2020). Widespread vaccination was crucial for mitigating severe disease and reducing healthcare system burden, yet vaccine hesitancy—the delay in acceptance or refusal of vaccination despite availability—remained a significant threat.

In the digital age, public opinion and health-related behaviors are increasingly shaped by discourse on social media platforms. These platforms can act as powerful vectors for both factual public health information and harmful misinformation, with research demonstrating a quantifiable negative impact of exposure to online misinformation on vaccination intent (Loomba et al., 2021). Online spaces often form "echo chambers," where users are primarily exposed to information that confirms their existing beliefs, potentially polarizing discussions and hardening opposition (Barberá et al., 2015).

Occupation is a critical social determinant of health, often serving as a proxy for education, income, and exposure risk. Traditionally, literature suggests that higher socioeconomic status (SES) and education levels correlate with higher vaccine acceptance (Fisher et al., 2020). This traditional understanding frames the central paradox explored in this study: if higher SES predicts greater acceptance, one might expect white-collar professional communities to exhibit more positive sentiment. If online discourse diverges from these established patterns—for instance, if white-collar communities express higher negativity—it suggests that online behavior may differ from general population behaviors, or that the nature of the negativity requires deeper examination.

The COVID-19 pandemic presented a complex picture regarding occupational risk and vaccine acceptance. While blue-collar and essential workers often faced higher exposure risks, studies indicated varied vaccination intent within these groups, influenced by factors such as historical mistrust in institutions and localized group norms (Daly & Robinson, 2021). Furthermore, political polarization in the United States often became a stronger predictor of vaccine stance than traditional SES indicators (Fridman et al., 2021).

Crucially, the landscape of this discourse was significantly altered by the introduction of employer and government vaccine mandates in 2021. Mandates introduced a critical confounding factor into the discourse; while aimed at increasing uptake, they also galvanized opposition by shifting the focus from medical efficacy to issues of autonomy, labor rights, and government overreach (Musumeci & Kates, 2021; Hamel et al., 2022). This policy context is critical, as resistance to mandates frequently transcended occupational categories but was articulated through different frameworks—legal and procedural challenges in professional sectors, and labor disputes in trades.

The social media platform Reddit, with its structure of distinct, topic-based communities known as "subreddits," provides a unique opportunity to study these group-specific conversations. By targeting subreddits dedicated to specific professions, it is possible to isolate and analyze the discourse within these occupational communities. This study leverages this platform to investigate the following research question: **How did sentiment towards COVID-19 vaccines differ between blue-collar and white-collar occupational communities on Reddit during the 2021 vaccine rollout?**

By analyzing both the quantitative sentiment and the qualitative nature of the discourse, this paper aims to provide nuanced insights that can inform more targeted and effective public health communication strategies.

---

## 2. Methodology

This study employed a mixed-methods approach combining programmatic data scraping via the Reddit API, Large Language Model (LLM)-based sentiment classification, and quantitative statistical analysis. The research pipeline was designed to capture, classify, and compare sentiment regarding COVID-19 vaccinations across distinct occupational communities on Reddit.

### 2.1 Data Collection and Sampling Strategy

Data was collected for the period between January 1, 2021, and December 31, 2021, capturing the primary phase of global COVID-19 vaccine rollout and mandates. The dataset was constructed by targeting 17 specific subreddits, categorized into two professional groups based on the nature of the labor discussed:

*   **Blue Collar (n=12):** Communities centered on manual or trade labor, including *Carpentry, electricians, Construction, Welding, Plumbing, Machinists, Truckers, AutoDetailing, Justrolledintotheshop, KitchenConfidential, ProtectAndServe,* and *Firefighting*.
*   **White Collar (n=5):** Communities centered on office or professional services, including *consulting, cscareerquestions, law, Accounting,* and *engineering*.

Data retrieval was performed using the Python Reddit API Wrapper (`praw`). A boolean search query was executed within each subreddit to identify relevant content containing at least one of the following keywords: `["vaccine", "vaccinated", "vaccination", "pfizer", "moderna", "j&j"]`.

To ensure content relevance, a strict filtering protocol was applied. For original submissions (posts), the keywords were required to appear in the title or self-text. For comments, the script traversed comment threads with a depth limit of 5 (using `replace_more(limit=5)`). Crucially, comments were only retained if the comment body explicitly contained one of the target keywords; general discussion comments lacking specific vaccine terminology were excluded to maintain topical precision.

The final dataset consisted of N=846 unique records, comprising 153 posts and 693 comments. The distribution between groups was 483 records for White Collar professions and 363 for Blue Collar professions.

### 2.2 Sentiment Classification

Sentiment analysis was conducted using Google's Gemini 2.5 Flash model (`gemini-2.5-flash`) via the `google-genai` library. An LLM approach was selected over lexicon-based methods (such as VADER) to better capture context and nuance in complex discussions regarding public health, a strength of modern LLMs (Zhang et al., 2023).

The classification process utilized a specific prompt instructing the model to determine the text's opinion specifically on "COVID vaccinations." The model was constrained to output a single label: `positive`, `neutral`, or `negative`. To ensure deterministic and reproducible results, the model temperature was set to 0.

Following classification, categorical labels were mapped to a numeric scale to facilitate statistical testing:
*   **Positive:** +1
*   **Neutral:** 0
*   **Negative:** -1

There were no missing sentiment scores in the final dataset; all 846 records were successfully classified.

### 2.3 Statistical Analysis

Quantitative analysis was performed using Python (`pandas`, `scipy`). The analysis focused on comparing the central tendency and distribution of sentiment between the two occupational categories.

1.  **Group Comparisons:** An independent two-sample t-test was utilized to compare the mean sentiment scores of Blue Collar and White Collar groups. Descriptive statistics, including means and 95% Confidence Intervals (CI), were calculated for both groups and for specific content types (posts vs. comments).
2.  **Distributional Analysis:** A Chi-square test of independence was performed to evaluate the relationship between occupational category and the frequency distribution of sentiment labels (positive, neutral, negative).
3.  **Correlation Analysis:** To assess the relationship between community approval and sentiment expression, Pearson (linear) and Spearman (monotonic) correlation coefficients were calculated between the `sentiment_score` and the Reddit `score` (Karma).

### 2.4 Visualization and Aggregation

To visualize trends, data was aggregated by month for time-series analysis and by subreddit for comparative ranking. Subreddit-level sentiment was visualized using weighted lollipop charts, where the size of the marker corresponded to the volume of activity (n) within that community. Additionally, box plots with strip overlays were generated to examine the distribution of Karma scores across sentiment categories, utilizing a symmetrical logarithmic scale to handle the high variance in Reddit scoring.

---

## 3. Results

### 3.1 Data Overview

The final dataset consisted of N=846 unique records generated between January 1, 2021, and December 31, 2021. The Large Language Model (Gemini 2.5) successfully classified 100% of the records, resulting in zero missing sentiment scores. The data was unevenly distributed across the two primary occupational categories, with the white-collar cohort accounting for 57.1% (n=483) of the sample and the blue-collar cohort accounting for 42.9% (n=363). In terms of content type, the dataset was predominantly composed of comments (n=693, 81.9%) rather than original posts (n=153, 18.1%).

### 3.2 Occupational Sentiment Differences

The primary analysis compared the mean sentiment scores regarding COVID-19 vaccination between white-collar and blue-collar communities. An independent samples t-test revealed a statistically significant difference in sentiment expression between the two groups (t = 4.025, p < 0.001).

The white-collar cohort exhibited a distinct negative sentiment bias, with a mean score of -0.240 (95% CI: [-0.308, -0.173]). In contrast, the blue-collar cohort displayed a mean sentiment effectively converging on neutrality at -0.006 (95% CI: [-0.098, 0.087]). The mean difference of 0.235 suggests that, on average, discussions within white-collar professional communities were significantly more critical or negative regarding vaccination topics than those in trade-based communities (Figure 1).

**Figure 1: Mean Sentiment Comparison: Blue Collar vs White Collar**
![Figure 1: Mean Sentiment Comparison](figures/fig_category_sentiment_comparison_corrected.png)

To understand the composition of these scores, a Chi-square test of independence was conducted on the categorical labels (positive, neutral, negative). The distribution of sentiment labels differed significantly by occupational category (χ² = 54.245, p < 0.001). While negative sentiment was prevalent in both groups (40.5% for blue-collar vs. 43.3% for white-collar), the divergence occurred in positive expression. The blue-collar group contained nearly double the proportion of positive records (39.9%) compared to the white-collar group (19.3%). Conversely, the white-collar group had a substantially higher proportion of neutral content (37.5%) compared to the blue-collar group (19.6%) (Figure 2).

**Figure 2: Sentiment Composition by Category**
![Figure 2: Sentiment Composition](figures/fig_sentiment_distribution_stacked.png)

### 3.3 Subreddit-Level Variance: The Illusion of the Average

While the aggregate statistics point to clear differences, a granular analysis at the subreddit level reveals that these category-wide averages are an "illusion," masking significant and meaningful variation within each group.

All five white-collar subreddits analyzed yielded negative mean sentiment scores. The most active communities in this category, *r/law* (n=199, μ=-0.307) and *r/Accounting* (n=152, μ=-0.283), drove the overall negative trend. Even the least negative community in this cohort, *r/cscareerquestions* (n=58), remained below neutrality with a mean of -0.052 (Figure 3).

**Figure 3: Sentiment Score by Subreddit: White Collar (Sorted by N)**
![Figure 3: White Collar Lollipop](figures/fig_sentiment_white_collar_lollipop_corrected.png)

Conversely, the blue-collar category displayed a polarized spectrum of sentiment. The most active community, *r/KitchenConfidential* (n=190), was notably positive with a mean of +0.163. Similarly, *r/Construction* (n=11) showed positive sentiment (μ=+0.182). However, this positivity was offset by strongly negative sentiment in communities such as *r/Machinists* (n=38, μ=-0.553) and *r/Truckers* (n=2, μ=-0.500). This indicates that the "neutral" aggregate score for blue-collar workers obscures a sharp divide between specific trades (Figure 4).

**Figure 4: Sentiment Score by Subreddit: Blue Collar (Sorted by N)**
![Figure 4: Blue Collar Lollipop](figures/fig_sentiment_blue_collar_lollipop_corrected.png)

### 3.4 Interaction of Content Type and Category

An analysis of content types (posts vs. comments) suggests that the divergence in sentiment is driven primarily by commentary rather than original submissions. Original posts across the entire dataset were consistently negative (μ = -0.222).

However, as illustrated in Figure 5, a divergence appears in the comment sections. White-collar comments remained deeply negative (mean ≈ -0.25), mirroring the sentiment of their posts. In contrast, blue-collar comments shifted toward positivity (mean ≈ +0.03). This interaction suggests that while the prompts (posts) initiated in both communities were negative, the ensuing dialogue (comments) became constructive or supportive in blue-collar spaces while remaining critical in white-collar spaces.

**Figure 5: Interaction of Content Type and Profession Category on Sentiment**
![Figure 5: Interaction](figures/fig_sentiment_type_category_interaction.png)

### 3.5 Temporal Trends

Longitudinal analysis over the 12-month period reveals high volatility in sentiment expression. Figure 6 tracks the monthly mean sentiment for both cohorts. The blue-collar cohort exhibited its highest positive peak in April 2021 (mean ≈ 0.58). The white-collar cohort showed significant downward volatility, reaching its lowest trough in late 2021 (mean ≈ -0.5). Throughout the observed period, the white-collar trend line rarely crossed into positive territory, whereas the blue-collar trend line oscillated frequently between positive and negative values.

**Figure 6: Monthly Sentiment Trends: Blue vs. White Collar (2021)**
![Figure 6: Time Series](figures/fig_sentiment_time_series_corrected.png)

### 3.6 Correlation with User Engagement

Finally, the relationship between sentiment and user engagement (measured by Karma score) was analyzed to determine if specific sentiments were incentivized by the community. A Pearson correlation analysis showed no linear relationship between sentiment scores and Karma (r = 0.024, p = 0.485).

A Spearman rank correlation was also performed to detect monotonic relationships. While this test yielded a statistically significant p-value (p = 0.006), the correlation coefficient was extremely weak (ρ = 0.094). This indicates that while a non-random relationship exists, the effect size is negligible. As shown in Figure 7, the distribution of Karma scores remains nearly identical across negative, neutral, and positive sentiment categories, suggesting that community approval (upvotes) was not contingent on the polarity of the opinion expressed regarding vaccines.

**Figure 7: Karma Score vs. Sentiment Category**
![Figure 7: Karma vs Sentiment](figures/fig_karma_vs_sentiment_corrected.png)

### 3.7 Qualitative Analysis of Discursive Themes

To understand the drivers of the observed sentiment variance, an exploratory qualitative analysis was conducted. This revealed that the nature of the discourse differed significantly between communities, often reflecting profession-specific concerns and frameworks.

#### 3.7.1 The Centrality of Mandates: Anti-Mandate vs. Anti-Vaccine

A portion of the negative sentiment across both categories was directed at coercion and employment consequences rather than the vaccine's efficacy or safety. This distinction is vital, as the negativity often reflected labor disputes or ideological objections to overreach rather than medical skepticism.

This was particularly prevalent in unionized or public service sectors, where opposition was framed as a labor rights issue. For example, in r/ProtectAndServe (Police), the discourse characterized the opposition as a contractual dispute:

> *"The media is trying to spin this as a bunch of dumb cops being against getting the vaccine. This is 100% about union and labor rights. The way the FOP sees it, the city is violating the contract... The reality is that at least 25% (probably more) of the people at risk of going into no pay status are already vaccinated."* — r/ProtectAndServe

Similar sentiments were found in trade communities, emphasizing autonomy and skepticism about employer coercion:

> *"Union electrician who was just informed I will be laid off Tuesday if I don't get the vaccine. Let me be clear. I am not an anti vaxer. I just believe in clinical trials."* — r/electricians

#### 3.7.2 White-Collar Discourse: Legalistic and Procedural Framing

The negativity observed in white-collar subreddits often adopted a detached, analytical frame, focusing on the legality, constitutionality, and implementation of vaccine policies.

In r/law (M = -0.31), the discourse was characterized by legal debates. Discussions frequently cited case law (e.g., Jacobson v. Massachusetts), questioned the statutory authority of regulatory bodies (like OSHA), and debated the constitutionality of mandates.

> *"This will certainly end up in court. Will this SCOTUS hear it? Will it overturn Jacobson v. Mass. against vaccine mandates or will it overturn Wickard v. Filburn saying OSHA is outside the commerce clause?"* — r/law

In r/consulting, negativity sometimes targeted the execution and logistics of vaccination programs rather than the vaccines themselves:

> *"44 million dollar system to track vaccinations. Deloitte pumped out some garbage that was slow and unusable."* — r/consulting

#### 3.7.3 Blue-Collar Discourse: Pragmatism, Risk, and Anxiety

Blue-collar discourse was more heterogeneous, reflecting diverse occupational realities.

**Pro-Social and Economic Pragmatism (r/KitchenConfidential):** The strongly positive sentiment in r/KitchenConfidential (M = 0.16) was framed around pragmatism, professional standards, and collective responsibility. Users argued that vaccination was necessary to keep restaurants open, protect coworkers, and ensure job security.

> *"If you're a chef and you give a single fuck about your craft, get the goddamn vaccine. Your food will be absolute shit when you catch COVID and can't smell or taste anything..."* — r/KitchenConfidential

**Occupational Risk Calculus:** A notable theme in some trades was the comparison of vaccine risk to the significant daily hazards inherent in their professions. Users compared the minor risk of the vaccine to significant occupational risks, which tended to minimize the perceived risk of the vaccine.

> *"It's pretty hilarious a bunch of Construction guys are worried about the safety of the vaccine but meanwhile will walk steel, weld without ventilation, bitch about the silica rules and not wear their seatbelt..."* — r/Construction

**Personal Health Anxiety Framing (r/Machinists):** In stark contrast, the negativity in r/Machinists (M = -0.55) centered on specific personal health anxieties and anecdotal adverse events. A prominent thread focused on tinnitus post-vaccination, a concern highly relevant to a profession where hearing damage is an occupational hazard.

> *"Developed very loud ringing after second Pfizer shot... Wouldn't have vaccinated if I knew it was going to do this. Its hell."* — r/Machinists

---

## 4. Discussion

### 4.1 Occupational Divergence in Vaccine Sentiment

The central finding of this study is the significant divergence in sentiment regarding COVID-19 vaccination between white-collar and blue-collar professional communities on Reddit. While prior literature has largely framed vaccine polarization through political or geographic lenses (Barberá et al., 2015), these results suggest that occupational identity—and specifically the nature of the labor performed—plays a critical mediating role. The white-collar cohort exhibited a pronounced negative mean sentiment (-0.240), whereas the blue-collar cohort converged on neutrality (-0.006), with a statistically significant difference (p < 0.001).

However, the qualitative nature of this "negativity" warrants careful sociological interpretation. The white-collar dataset was dominated by communities such as *r/law* (n=199, μ=-0.307) and *r/Accounting* (n=152, μ=-0.283). Given the professional focus of these subreddits, it is plausible that the observed negative sentiment reflects administrative friction rather than ideological opposition to the vaccine itself. In these "laptop class" professions, the discourse likely centered on the logistical complexities of mandates, liability frameworks, and remote work policies (Musumeci & Kates, 2021). Conversely, the blue-collar cohort, particularly in service-oriented sectors, may have viewed vaccination as a pragmatic mechanism for economic reopening.

### 4.2 The Interaction of Content Type and Discourse Dynamics

A granular analysis of content types reveals a distinct interaction effect that further complicates the binary of "pro-vax" vs. "anti-vax" sentiment. While original posts (submissions) were consistently negative across both categories, a sharp divergence occurred in the comment sections (Figure 5).

White-collar comments remained deeply negative (-0.25), closely mirroring the sentiment of the posts they replied to (-0.22). This suggests a pattern of "complaint reinforcement," where threads in communities like *r/consulting* or *r/cscareerquestions* function as echo chambers for professional grievances. In contrast, blue-collar comments broke from the negative trend of their parent posts to become the only positive subset in the study (μ=+0.03). This inversion implies a self-correcting or community-policing dynamic within trade subreddits. When a user in a blue-collar forum posted negatively about vaccines (potentially expressing hesitation or sharing misinformation), the community response in the comments tended to be corrective or supportive of vaccination. This finding challenges the stereotype of trade communities as monolithic hubs of vaccine resistance (Daly & Robinson, 2021), suggesting instead a vigorous internal debate where community consensus often leaned toward pragmatism.

### 4.3 Sub-Community Variations: Service vs. Solitary Trades

Within the blue-collar category, sentiment was not uniform. Variation appears to be driven by the degree of social interaction required by the trade, supporting the hypothesis that "economic necessity" drives positive sentiment in service sectors.

Among the high-volume communities analyzed, *r/KitchenConfidential* (hospitality workers) displayed the highest positive sentiment (μ=+0.163, n=190). For kitchen staff, for whom remote work is impossible, the vaccine represented the only pathway to normalizing restaurant operations and securing wages. This stands in stark contrast to *r/Machinists* (n=38), which exhibited the most negative sentiment among the active trade groups (μ=-0.553). Machinists often work in more solitary, industrial environments with less direct public interaction, potentially reducing the perceived immediate economic benefit of vaccination or the social pressure to comply.

### 4.4 The Independence of Karma and Sentiment

Contrary to the hypothesis that Reddit functions as a polarization engine that rewards extreme views, this study found no significant correlation between sentiment score and Karma score (Pearson r=0.024). The distribution of Karma was nearly identical across positive, neutral, and negative contributions (Figure 7). This suggests that during 2021, these professional communities did not systematically amplify one side of the vaccine debate over the other through upvoting mechanisms. Both critical and supportive viewpoints received comparable levels of visibility, indicating that the "echo chamber" effect may be driven more by the volume of contributions rather than the algorithmic amplification of those contributions.

### 4.5 Limitations

Several methodological limitations constrain the generalizability of these findings.

**Representativeness:** The user base of Reddit is not representative of the general population, often skewing younger and male. The findings reflect the views of active users within these specific online communities and are not generalizable to all blue-collar and white-collar workers.

**Data Collection:** The reliance on a specific set of keywords means the analysis is sensitive to the terminology used. The keyword filtering strategy applied a strict inclusion criterion: not only posts but also comments were required to contain specific vaccine-related keywords to be included. This approach optimized for topical relevance but likely excluded a significant volume of contextual discourse.

**LLM Classification Nuance:** While the Gemini 2.5 model showed high efficacy, nuanced sarcasm or domain-specific jargon may have been occasionally misclassified. The analysis reveals that in certain situations, sentiments towards COVID vaccines may be miscategorized—for example, comments using strongly aggressive language may be scored as negative even if the underlying attitude towards vaccines is positive.

---

## 5. Conclusion

This study provides a granular examination of how occupational identity influenced digital discourse regarding COVID-19 vaccinations during the pivotal rollout phase of 2021. By analyzing N=846 contributions across 17 profession-specific subreddits, this research challenges monolithic narratives regarding online vaccine hesitancy.

### 5.1 Synthesis of Findings

The most significant finding of this research is the statistical divergence in sentiment between white-collar and blue-collar communities. Contrary to stereotypes often associated with working-class vaccine resistance, the blue-collar cohort displayed a sentiment profile converging on neutrality (μ = -0.006), with specific trade communities such as *r/KitchenConfidential* exhibiting net positive sentiment (+0.163). In contrast, white-collar communities exhibited a statistically significant negative bias (μ = -0.240, p < 0.001).

This divergence was further elucidated by the interaction between content type and occupational category. While original submissions (posts) were universally critical across all sectors, the comment sections revealed a stark behavioral split. Blue-collar comments trended slightly positive, suggesting a community dynamic where peer-to-peer interaction reinforced compliance or pragmatic acceptance. Conversely, white-collar comments remained deeply negative, mirroring the sentiment of the original posts. Furthermore, the lack of correlation between sentiment and Karma scores (r=0.024) indicates that these communities did not mechanically reward polarization.

### 5.2 Sociological Implications

These results suggest that the "infodemic" was not experienced uniformly across the labor market. The relative positivity of service-oriented blue-collar communities supports the theory of "safety capital," where vaccination was framed not merely as a health intervention but as an economic necessity for the resumption of labor. For chefs, servers, and tradespeople, the vaccine represented a pathway to reopening. Conversely, the negativity observed in "laptop class" subreddits (*r/law*, *r/Accounting*) implies that for remote-capable professionals, the vaccine mandates were often discussed as bureaucratic impositions, liability puzzles, or logistical hurdles rather than existential economic enablers.

### 5.3 Public Health Implications

The primary implication for public health is clear: one-size-fits-all communication strategies are destined to fail. To effectively build trust and encourage vaccine uptake, public health agencies must move beyond broad demographic targeting and engage in a form of "discursive listening." By understanding and addressing the specific conversational frames that dominate different communities, messaging can be tailored to be more resonant, respectful, and ultimately, more effective.

The qualitative findings provide critical context: the negativity in r/law was not "anti-vaccine" in a medical sense but "anti-mandate" in a legal one. Messaging that focuses on vaccine safety and efficacy would likely be ineffective in this community, where the core concerns are constitutional and procedural. In contrast, the negativity in r/Machinists was deeply personal and rooted in specific health fears relevant to their trade. Messaging for this group should acknowledge these specific anxieties and provide clear information on known side effects.

### 5.4 Future Directions

Future research in digital epidemiology should extend beyond political binaries to include socioeconomic and occupational variables. Longitudinal studies tracking these same communities into 2022 and 2023 could reveal how sentiment evolved as mandates were lifted and the virus became endemic. Additionally, comparative analyses across different platforms—contrasting the pseudonymous, community-governed nature of Reddit with the identity-forward professional environment of LinkedIn—would provide a more holistic understanding of how professional reputation influences online health expressions.

In conclusion, this study underscores that professional identity acts as a critical filter for public health messaging. Understanding the distinct concerns of occupational communities—whether they be the economic pragmatism of the trades or the administrative skepticism of the professions—is essential for crafting targeted, effective public health communication strategies in future crises.

---

## References

Barberá, P., Jost, J. T., Nagler, J., Tucker, J. A., & Bonneau, R. (2015). Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber? *Psychological Science*, 26(10), 1531–1542. https://doi.org/10.1177/0956797615594620

Daly, M., & Robinson, E. (2021). Willingness to Vaccinate Against COVID-19 in the U.S.: Representative Longitudinal Evidence From April to October 2020. *American Journal of Preventive Medicine*, 60(6), 766–773. https://doi.org/10.1016/j.amepre.2021.01.008

Fisher, K. A., Bloomstone, S. J., Walder, J., Crawford, S., Fouayzi, H., & Mazor, K. M. (2020). Attitudes Toward a Potential SARS-CoV-2 Vaccine: A Survey of U.S. Adults. *Annals of Internal Medicine*, 173(12), 964–973. https://doi.org/10.7326/M20-3569

Fridman, A., Gershon, R., & Gneezy, A. (2021). COVID-19 and vaccine hesitancy: A longitudinal study. *PLoS ONE*, 16(4), e0250123. https://doi.org/10.1371/journal.pone.0250123

Hamel, L., Lopes, L., Kearney, A., & Brodie, M. (2022). KFF COVID-19 vaccine monitor: March 2021. *KFF*. https://www.kff.org/coronavirus-covid-19/poll-finding/kff-covid-19-vaccine-monitor-march-2021/

Loomba, S., de Figueiredo, A., Piatek, S. J., de Graaf, K., & Larson, H. J. (2021). Measuring the impact of COVID-19 vaccine misinformation on vaccination intent in the UK and USA. *Nature Human Behaviour*, 5, 337–348. https://doi.org/10.1038/s41562-021-01056-1

Musumeci, M., & Kates, J. (2021). Key questions about COVID-19 vaccine mandates. *KFF*. https://www.kff.org/coronavirus-covid-19/issue-brief/key-questions-about-covid-19-vaccine-mandates/

Zhang, W., Deng, Y., Liu, B., Pan, S. J., & Bing, L. (2023). Sentiment Analysis in the Era of Large Language Models: A Reality Check. *arXiv preprint arXiv:2305.11489*. https://arxiv.org/abs/2305.11489

Zarocostas, J. (2020). How to fight an infodemic. *The Lancet*, 395(10225), 676. https://doi.org/10.1016/S0140-6736(20)30461-X
