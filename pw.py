import streamlit as st
#from PIL import Image

# ------------------ Page config ------------------
st.set_page_config(
    page_title="ZhaonianQu",
    layout="centered"
)


st.markdown(
    """
    <style>
    
    .block-container{
        padding-top: 150px !important;  /* adjust this number */
    }
    
    /* Sticky header container (works for title + tabs area) */
    .sticky-header {
        position: fixed;
        top: 20px;
        width: 100%;
        background: white;
        z-index: 999;
        padding-top: 10px;
        padding-bottom: 8px;
    }

    /* Make the tabs bar sticky too */
    div[data-baseweb="tab-list"] {
        position: fixed;
        top: 100px;
        left: 0;
        right: 0;
        width: 100vw;
        background: white;
        z-index: 999;
        padding-bottom: 6px;
        border-bottom: 1px solid #e6e6e6;
        justify-content: center;
    }
    
    button[data-baseweb="tab"] {
        font-size: 120px;
        font-weight: 600;
        padding: 30px 50px;
        margin: 0 2px;
        letter-spacing: 0.0em;
    }

    div[data-testid="stTabs"] > div:first-child {
        border-bottom: none;
    }
    div[data-testid="stTabs"] > div:last-child{
      border-top: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# ---- Sticky title ----
st.markdown('<div class="sticky-header"><h1 style="margin:0;">Zhaonian (John) Qu</h1></div>',
            unsafe_allow_html=True)


page= st.tabs(
    ["Home", "Research", "Publications","Contact"],
)



with page[0]:

    st.subheader("Bio")
    col1, col2 = st.columns([1, 2], gap="medium")
    with col1:
        st.image("profile.png", width=200)  # or width=420
    with col2:
        st.markdown(
            """
            I am a PhD candidate working on **oil droplet size distribution (DSD)** of **oil–gas–water multiphase flows** using 
            **CFD–population balnace model (PBM) coupling** method to invesigate the subsea spilled oil transport.\n
            """
        )
        st.markdown(
        """
        - **[Google scholar](https://scholar.google.com/citations?user=QQgpGbcAAAAJ&hl=en)**\n

        - **[ResearchGate](https://www.researchgate.net/profile/Zhaonian-Qu-2?ev=hdr_xprf)**\n
        
        - **[Linkedin](https://www.linkedin.com/in/zhaonian-qu-b88469235/)** \n

        """
        )
    st.markdown("---")
    st.subheader("Education")
    st.markdown(
        """
        - **[New Jersey Institute of Technology](https://www.njit.edu/)**, Newark, USA\n
        PhD candidate in Environmental Engineering, 09/2023 – present 

        - **[Concordia University](https://www.concordia.ca/)**, Montreal, Canada\n
        Master’s in Civil and Environmental Engineering, 09/2021 – 08/2023 
        
        - **[Shandong University](https://www.en.sdu.edu.cn/)**, Qingdao, China \n
        Bachelor’s in Environmental Engineering, 09/2017 – 06/2021

        """
    )
    st.markdown("---")
    st.subheader("Awards")
    st.markdown(
        """
        - Gary Thomas Fellowship of New Jersey Institute of Technology (2024)
        - The F.A. Gerard Prize of Concordia University (2024)
        - Gary Thomas Fellowship of New Jersey Institute of Technology (2023)
        - Concordia University Conference and Exposition Award (2023)
        - Special Recognition Award of International Oil Spill Science Conference (2022)
        - Concordia Split Merit Scholarship (2021)
        - First Prize, Guocai Cup English Writing Competition, Shandong Division of Foreign Research Institute (Provincial Level)   (2019) 
        - Scholarship of Shandong University (2019)
        - Scholarship of Shandong University (2018) 
        """
    )
        

# ------------------ Research ------------------
with page[1]:
    st.subheader("Current research area")

    st.markdown(
        """
        **Primary Areas**
        - Multiphase flow simulation
        - Population Balance Modeling (PBM)
        - Droplet recognization algorithm\n
        Advised by [Dr. Michel Boufadel](https://people.njit.edu/profile/boufadel)\n
        **Tools**
        - OpenFOAM/ Ansys Fluent
        - C++/ Python / MATLAB
        """
    )
    
    st.subheader("Previous research area")

    st.markdown(
        """
        **Master's dissertation**\n
        Infiltration of Spilled Oil in Soil under Various Environmental Conditions\n 
        Advised by [Dr. Chunjing An](https://anlab.ca/)
        
        **Tools**
        - GC-FID
        """
    )

# ------------------ Publications ------------------
with page[2]:
    st.subheader("Publications")

    st.markdown(
        """
        - [Oil droplet from blowouts: Role of gas and dispersant](https://doi.org/10.1016/j.ijmultiphaseflow.2025.105488)\n
          Ruixue Liu, Subhamoy Gupta, Cosan Daskiran, Changyang Tan, Diego Muriel, Joseph Katz, **Zhaonian Qu**, Kenneth Lee, Michel Boufadel, International Journal of Multiphase Flow (Elsevier), 105488 (2025)
        
        - [Simulation of subsurface mechanical dispersion (SSMD) of oil by a water jet](https://doi.org/10.1016/j.marpolbul.2025.117586)\n
          **Zhaonian Qu**, Tanvir Al Farid, Scott Socolofsky, Timothy Steffek, Michel Boufadel, Marine Pollution Bulletin (Elsevier), 213, 117586 (2025)
         
        - [Investigation of the Vertical Infiltration of Spilled Oil in Soil Impacted by Root Netting and Surface Rainfall](https://doi.org/10.1061/JOEEDU.EEENG-7684)\n
          **Zhaonian Qu**, Rengyu Yue, Huifang Bi, Shan Zhao, Michel Boufadel, Xiujuan Chen, and Chunjiang An, Journal of Environmental Engineering (American Society of Civil Engineers), 150(8), 04024039 (2024)
        
        - [Two birds with one stone: A dual-functional washing fluid for shoreline oil spill response](https://doi.org/10.1016/j.scitotenv.2023.165325)\n
          Rengyu Yue, Zhibin Ye, Baiyu Zhang, Chunjiang An, **Zhaonian Qu**, Shuyan Wan, ES&T Engineering (ACS), 4(2), 445-454 (2023)
          
        - [Assessment of the Infiltration of Water-In-Oil Emulsion into Soil after Spill Incidents](https://doi.org/10.1016/j.scitotenv.2023.165325)\n
          **Zhaonian Qu**, Chunjiang An, Rengyu Yue, Huifang Bi, and Shan Zhao, Science of The Total Environment (Elsevier), 896, 165325 (2023)
          
        - [Preparation, Characteristics, and Performance of the Microemulsion System in the Removal of Oil from Beach Sand](https://doi.org/10.1016/j.marpolbul.2023.115234)\n
          Huifang Bi, Catherine N. Mulligan, Kenneth Lee, Chunjiang An, Jiyuan Wen, Xiaohan Yang, Linxiang Lyu, and **Zhaonian Qu**, Marine Pollution Bulletin (Elsevier), 10(8), 1111 (2023)
         
        - [Exploring the Use of Sodium Caseinate-Assisted Responsive Separation for the Treatment of Washing Effluents in Shoreline Oil Spill Response](https://doi.org/10.1016/j.scitotenv.2023.162363)\n 
          Rengyu Yue, Zhibin Ye, Sichen Gao, Yiqi Cao, Kenneth Lee, Chunjiang An, **Zhaonian Qu**, and Shuyan Wan, Science of the Total Environment (Elsevier), 873,162363 (2023)
          
        - [A pH-Responsive Phosphoprotein Washing Fluid for the Removal of Phenanthrene from Contaminated Peat Moss in the Cold Region](https://doi.org/10.1016/j.chemosphere.2022.137389)\n
          Rengyu Yue, Chunjiang An, Zhibin Ye, Xixi Li, Qing Li, Peng Zhang, **Zhaonian Qu**, and Shuyan Wan, Chemosphere (Elsevier), 313, 137389 (2022)
          
        - [Emerging Marine Pollution from Container Ship Accidents: Risk Characteristics, Response Strategies, and Regulation Advancements](https://doi.org/10.1016/j.jclepro.2022.134266)\n
          Shuyan Wan, Xiaohan Yang, Xinya Chen, **Zhaonian Qu**, Chunjiang An, Baiyu Zhang, Kenneth Lee, and Huifang Bi, Journal of Cleaner Production (Elsevier), 376, 134266 (2022).
          
        - [Exploring the Characteristics, Performance, and Mechanisms of a Magnetic-mediated Washing Fluid for the Cleanup of Oiled Beach Sand](https://doi.org/10.1016/j.jhazmat.2022.129447)\n
          Rengyu Yue, Chunjiang An, Zhibin Ye, Xiujuan Chen, Kenneth Lee, Kaiqiang Zhang, Shuyan Wan, and **Zhaonian Qu**, Journal of Hazardous Materials (Elsevier), 438,129447 (2022)
          
        - [Application of Phase-Selective Organogelators (PSOGs) for Marine Oil Spill Remediation](https://doi.org/10.3390/jmse10081111)\n
          Huifang Bi, Chunjiang An, Catherine N. Mulligan, Zhi Chen, Kenneth Lee, Jiyuan Wen, **Zhaonian Qu**, and Xinya Chen, Journal of Marine Science and Engineering (MDPI), 10(8):1111 (2022)
        
        - [An Experimental and Modeling Study on the Penetration of Spilled Oil into Thawing Frozen Soil](https://doi.org/10.1039/D2EM00368F)\n
          **Zhaonian Qu**, Chunjiang An, Zhu Mei, Rengyu Yue, Shan Zhao, Qi Feng, Mengfan Cai, and Jiyuan Wen, Environmental Science: Impacts and Processes (Royal Society of Chemistry), 24, 2398- 2408 (2022)
         
        """
    )

# ------------------ Contact ------------------
with page[3]:
    st.subheader("Contact")

    st.markdown(
        """
         **Email**: zhaonian.qu99@gmail.com  
        """

    )

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            st.success("Message sent (placeholder)")

# ------------------ Footer ------------------
st.markdown("---")
st.caption("© 2025 Zhaonian (John) Qu")
