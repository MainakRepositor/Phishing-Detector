import streamlit as st
import pickle
import pandas as pd
from extract_features import ExtractFeatures
from PIL import Image


import streamlit as st

st.markdown(
    "<div style='display: flex; align-items: center; margin-bottom: -35px;'>"
    "<h1 style='color:#003E7F; margin-right: 10px;'> Unmasking Phishing Websites:</h1>"
    "</div>"
    "<h1 style='color:orange; margin-left: 10px;'>A Machine Learning Approach</h1>"
    "</div>",
    unsafe_allow_html=True
)

image=Image.open('cybersecpic.jpeg')
width=750
height=500
image_new=image.resize((width,height))
st.image(image_new)

st.markdown("### *Specifications Table*")
data = {
    'Attribute': [
        'Subject', 'Specific subject area', 'Type of data', 'How data were acquired', 'Data format',
        'Parameters for data collection', 'Description of data collection', 'Data source location',
        'Data accessibility', 'Related research article'
    ],
    'Value': [
        'Computer Science', 'Artificial Intelligence', 'csv file',
        'Data were acquired through the publicly available lists of phishing and legitimate websites, from which the features presented in the datasets were extracted.',
        'Raw: csv file',
        'For the phishing websites, only the ones from the PhishTank registry were included, which are verified from multiple users. For the legitimate websites, we included the websites from publicly available, community labeled and organized lists [1], and from the Alexa top ranking websites.',
        'The data is comprised of the features extracted from the collections of websites addresses. The data in total consists of 111 features, 96 of which are extracted from the website address itself, while the remaining 15 features were extracted using custom Python code.',
        'Worldwide',
        'Repository name: Mendeley Data\nData identification number: 10.17632/72ptz43s9v.1\nDirect URL to data: [https://doi.org/10.17632/72ptz43s9v.1](https://doi.org/10.17632/72ptz43s9v.1)',
        'Vrbančič, Grega, Iztok Fister Jr, and Vili Podgorelec. “Parameter setting for deep neural networks using swarm intelligence on phishing websites classification.” International Journal on Artificial Intelligence Tools 28.06 (2019): 1960008. DOI:10.1142/S021821301960008X'
    ]
}
df = pd.DataFrame(data)
st.table(df)

st.markdown("### *Abstract*")
st.markdown("Phishing stands for a fraudulent process, where an attacker tries to obtain sensitive information from the victim. Usually, these kinds of attacks are done via emails, text messages, or websites. Phishing websites, which are nowadays in a considerable rise, have the same look as legitimate sites. However, their backend is designed to collect sensitive information that is inputted by the victim. Discovering and detecting phishing websites has recently also gained the machine learning community’s attention, which has built the models and performed classifications of phishing websites. This paper presents two dataset variations that consist of 58,645 and 88,647 websites labeled as legitimate or phishing and allow the researchers to train their classification models, build phishing detection systems, and mining association rules.")
st.markdown("### *Value of the Data*")
st.markdown("- These data consist of a collection of legitimate, as well as phishing website instances. Each website is represented by the set of features that denote whether the website is legitimate or not. Data can serve as input for the machine learning process.")
st.markdown("- Machine learning and data mining researchers can benefit from these datasets, while also computer security researchers and practitioners. Computer security enthusiasts can find these datasets interesting for building firewalls, intelligent ad blockers, and malware detection systems.")            
st.markdown("- This dataset can help researchers and practitioners easily build classification models in systems preventing phishing attacks since the presented datasets feature the attributes which can be easily extracted.")
st.markdown("- Finally, the provided datasets could also be used as a performance benchmark for developing state-of-the-art machine learning methods for the task of phishing websites classification.")

st.markdown("### *1. Data Description*")
st.markdown("The presented dataset was collected and prepared for the purpose of building and evaluating various classification methods for the task of detecting phishing websites based on the uniform resource locator (URL) properties, URL resolving metrics, and external services. The attributes of the prepared dataset can be divided into six groups:")
st.markdown("- attributes based on the whole URL properties presented in Table 1,")

# Define the table data
st.markdown('#### Table 1. Dataset attributes based on URL.')
data = {
    'Nr.': list(range(1, 21)),
    'Attribute': [
        'qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 'qty_questionmark_url',
        'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url',
        'qty_tilde_url', 'qty_comma_url', 'qty_plus_url', 'qty_asterisk_url', 'qty_hashtag_url',
        'qty_dollar_url', 'qty_percent_url', 'qty_tld_url', 'length_url', 'email_in_url'
    ],
    'Format': [
        'Number of "." signs', 'Number of "-" signs', 'Number of "_" signs', 'Number of "/" signs',
        'Number of "?" signs', 'Number of "=" signs', 'Number of "@" signs', 'Number of "&" signs',
        'Number of "!" signs', 'Number of " " signs', 'Number of "~" signs', 'Number of "," signs',
        'Number of "+" signs', 'Number of "*" signs', 'Number of "#" signs', 'Number of "$" signs',
        'Number of "%" signs', 'Top level domain character length', 'Number of characters', 'Is email present'
    ],
    'Description': ['Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Boolean'],
    'Values': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '[0, 1]']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)
# Display the table using st.table
st.table(df)

st.markdown("- attributes based on the domain properties presented in Table 2,")
st.markdown('#### Table 2. Dataset attributes based on domain URL.')

data = {
    'Nr.': list(range(1, 22)),
    'Attribute': [
        'qty_dot_domain', 'qty_hyphen_domain', 'qty_underline_domain', 'qty_slash_domain',
        'qty_questionmark_domain', 'qty_equal_domain', 'qty_at_domain', 'qty_and_domain',
        'qty_exclamation_domain', 'qty_space_domain', 'qty_tilde_domain', 'qty_comma_domain',
        'qty_plus_domain', 'qty_asterisk_domain', 'qty_hashtag_domain', 'qty_dollar_domain',
        'qty_percent_domain', 'qty_vowels_domain', 'domain_length', 'domain_in_ip', 'server_client_domain'
    ],
    'Format': [
        'Number of "." signs', 'Number of "-" signs', 'Number of "_" signs', 'Number of "/" signs',
        'Number of "?" signs', 'Number of "=" signs', 'Number of "@" signs', 'Number of "&" signs',
        'Number of "!" signs', 'Number of " " signs', 'Number of "~" signs', 'Number of "," signs',
        'Number of "+" signs', 'Number of "*" signs', 'Number of "#" signs', 'Number of "$" signs',
        'Number of "%" signs', 'Number of vowels', 'Number of domain characters',
        'URL domain in IP address format', '"server" or "client" in domain'
    ],
    'Description': ['Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Boolean', 'Boolean'],
    'Values': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '[0, 1]', '[0, 1]']
}


df = pd.DataFrame(data)
st.table(df)

# TABLE 3   
st.markdown('- attributes based on the URL directory properties presented in Table 3,')
st.markdown('#### Table 3. Dataset attributes based on URL directory.')

data = {
    'Nr.': list(range(1, 19)),
    'Attribute': [
        'qty_dot_directory', 'qty_hyphen_directory', 'qty_underline_directory', 'qty_slash_directory',
        'qty_questionmark_directory', 'qty_equal_directory', 'qty_at_directory', 'qty_and_directory',
        'qty_exclamation_directory', 'qty_space_directory', 'qty_tilde_directory', 'qty_comma_directory',
        'qty_plus_directory', 'qty_asterisk_directory', 'qty_hashtag_directory', 'qty_dollar_directory',
        'qty_percent_directory', 'directory_length'
    ],
    'Format': [
        'Number of "." signs', 'Number of "-" signs', 'Number of "_" signs', 'Number of "/" signs',
        'Number of "?" signs', 'Number of "=" signs', 'Number of "@" signs', 'Number of "&" signs',
        'Number of "!" signs', 'Number of " " signs', 'Number of "~" signs', 'Number of "," signs',
        'Number of "+" signs', 'Number of "*" signs', 'Number of "#" signs', 'Number of "$" signs',
        'Number of "%" signs', 'Number of directory characters'
    ],
    'Description': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    'Values': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
}

df = pd.DataFrame(data)
st.table(df)
    
# TABLE 4  
st.markdown('- attributes based on the URL file properties presented in Table 4,')
st.markdown('#### Table 4. Dataset attributes based on URL file name.')

data = {
    'Nr.': list(range(1, 19)),
    'Attribute': [
        'qty_dot_file', 'qty_hyphen_file', 'qty_underline_file', 'qty_slash_file',
        'qty_questionmark_file', 'qty_equal_file', 'qty_at_file', 'qty_and_file',
        'qty_exclamation_file', 'qty_space_file', 'qty_tilde_file', 'qty_comma_file',
        'qty_plus_file', 'qty_asterisk_file', 'qty_hashtag_file', 'qty_dollar_file',
        'qty_percent_file', 'file_length'
    ],
    'Format': [
        'Number of "." signs', 'Number of "-" signs', 'Number of "_" signs', 'Number of "/" signs',
        'Number of "?" signs', 'Number of "=" signs', 'Number of "@" signs', 'Number of "&" signs',
        'Number of "!" signs', 'Number of " " signs', 'Number of "~" signs', 'Number of "," signs',
        'Number of "+" signs', 'Number of "*" signs', 'Number of "#" signs', 'Number of "$" signs',
        'Number of "%" signs', 'Number of file name characters'
    ],
    'Description': ['Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric'],
    'Values': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
}

df = pd.DataFrame(data)
st.table(df)

# TABLE 5  
st.markdown('- attributes based on the URL parameter properties presented in Table 5, and')
st.markdown('#### Table 5. Dataset attributes based on URL parameters.')
    
data = {
    'Nr.': list(range(1, 19)),
    'Attribute': [
        'qty_dot_file', 'qty_hyphen_file', 'qty_underline_file', 'qty_slash_file',
        'qty_questionmark_file', 'qty_equal_file', 'qty_at_file', 'qty_and_file',
        'qty_exclamation_file', 'qty_space_file', 'qty_tilde_file', 'qty_comma_file',
        'qty_plus_file', 'qty_asterisk_file', 'qty_hashtag_file', 'qty_dollar_file',
        'qty_percent_file', 'file_length'
    ],
    'Format': [
        'Number of "." signs', 'Number of "-" signs', 'Number of "_" signs', 'Number of "/" signs',
        'Number of "?" signs', 'Number of "=" signs', 'Number of "@" signs', 'Number of "&" signs',
        'Number of "!" signs', 'Number of " " signs', 'Number of "~" signs', 'Number of "," signs',
        'Number of "+" signs', 'Number of "*" signs', 'Number of "#" signs', 'Number of "$" signs',
        'Number of "%" signs', 'Number of file name characters'
    ],
    'Description': ['Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Boolean', 'Numeric'],
    'Values': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
}   

df = pd.DataFrame(data)
st.table(df)    


# TABLE 6
st.markdown('- attributes based on the URL resolving data and external metrics presented in Table 6.')
st.markdown('#### Table 6. Dataset attributes based on resolving URL and external services.')

data = {
    'Nr.': list(range(1, 16)),
    'Attribute': [
        'time_response', 'domain_spf', 'asn_ip', 'time_domain_activation', 'time_domain_expiration',
        'qty_ip_resolved', 'qty_nameservers', 'qty_mx_servers', 'ttl_hostname', 'tls_ssl_certificate',
        'qty_redirects', 'url_google_index', 'domain_google_index', 'url_shortened', 'phishing'
    ],
    'Format': [
        'Domain lookup time response', 'Domain has SPF', 'ASN', 'Domain activation time (in days)',
        'Domain expiration time (in days)', 'Number of resolved IPs', 'Number of resolved NS',
        'Number of MX servers', 'Time-To-Live (TTL)', 'Has valid TLS/SSL certificate', 'Number of redirects',
        'Is URL indexed on Google', 'Is domain indexed on Google', 'Is URL shortened',
        'Is phishing website'
    ],
    'Description': [
        'Numeric', 'Boolean', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric',
        'Numeric', 'Boolean', 'Numeric', 'Boolean', 'Boolean', 'Boolean', 'Boolean'
    ],
    'Values': ['', '[0, 1]', '', '', '', '', '', '', '', '[0, 1]', '', '[0, 1]', '[0, 1]', '[0, 1]','']
}

df = pd.DataFrame(data)
st.table(df)

st.markdown('The first group is based on the values of the attributes on the whole URL string, while the values of the following four groups are based on the particular sub-strings, as presented in Figure 1. The last group attributes are based on the URL resolve metrics as well as on the external services such as Google search index.')

image=Image.open('pic1.jpg')
st.image(image, width=500)
st.markdown("##### Fig. 1. Separation of the whole URL string into sub-strings.")
st.markdown("The dataset in total features 111 attributes excluding the target phishing attribute, which denotes whether the particular instance is legitimate (value 0) or phishing (value 1). We prepared two variations of the dataset, the one where the total number of instances is 58,645 and the balance between the target classes in more or less balanced with 30,647 instances labeled as phishing websites and 27,998 instances labeled as legitimate. The second variant of the dataset is comprised of 88,647 instances with 30,647 instances labeled as phishing and 58,000 instances labeled as legitimate, the purpose of which is to mimic the real-world situation where there are more legitimate websites present. The distribution between the classes of both dataset variants is presented in Figure 2.")

image=Image.open('pic2.jpg')
st.image(image, width=500)
st.markdown("##### Fig. 2. The distribution between classes for both dataset variations. The dataset_full denotes the larger dataset, while the dataset_small denotes the smaller dataset variation. The target class 0 denotes legitimate websites while the target class 1 denotes the phishing websites.")

st.markdown("### *2. Experimental Design, Materials and Methods*")
st.markdown("In the process of preparing the phishing websites datasets variants presented in [2], we followed common steps which were also used in the dataset preparation process of similar datasets presented by Mohammad et al. [3] and Abdelhamid et al. [4].1234567")
st.markdown("In the manner of such preparation process, we firstly collected a list of a total of 30,647 confirmed phishing URLs from the Phishtank [5] website. On the other hand, the list of legitimate URLs was obtained from Alexa ranking website8 from which we gathered 58,000 legitimate website URLs. Additionally, we have also obtained the list of 27,998 community labeled and organized URLs [1], which are the URLs pointing to the objectively reported news and are in that manner also legitimate.")
st.markdown("From the URL lists of phishing and legitimate websites, we prepared, as already presented, two variants of the dataset. The smaller, more balanced dataset dataset_small comprises instances of extracted features from Phishtank URLs and instances of extracted features from community labeled and organized URLs representing legitimate ones. On the other hand, the larger, more unbalanced dataset consists of all of the instances from the dataset_small and the additional instances of extracted features from Alexa top sites URL list.")
st.markdown("The complete process of extracting the features from the list of collected website addresses was conducted automatically, using a Python script. The extracting process is outlined in Algorithm 1. Such procedure was conducted in total two times, each time given different set of website addresses as already described. The final outcome reflects in two csv files containing extracted features. The csv files are handy and easy to work with various tools and programming libraries.")


image=Image.open('pic3.jpg')
st.image(image, width=500)
st.markdown("##### Algorithm 1. Feature extraction process")

st.markdown("### *Declaration of Competing Interest*")
st.markdown("The authors declare that they have no known competing financial interests or personal relationships which have, or could be perceived to have, influenced the work reported in this article.")

st.markdown("### *Acknowledgments*")
st.markdown("Authors acknowledge the financial support from the Slovenian Research Agency (Research Core Funding No. P2-0057).")

st.markdown("### *Reference*")

st.write("""This research is based on this paper [here](https://www.sciencedirect.com/science/article/pii/S2352340920313202#fig0001)""")
