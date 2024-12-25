import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from pprint import pprint

information = """
Pratap Singh I (9 May 1540 - 19 January 1597), popularly known as Maharana Pratap, was king of the Kingdom of Mewar, in north-western India in 
the present-day state of Rajasthan, from 1572 until his death in 1597. He is notable for leading the Rajput resistance against the expansionist 
policy of the Mughal Emperor Akbar including the Battle of Haldighati and the Battle of Dewair.

Early life and accession:
Maharana Pratap was born to Udai Singh II of Mewar and Jaiwanta Bai in 1540, the year in which Udai Singh ascended to the throne after 
defeating Vanvir Singh.[5][6][7] His younger brothers were Shakti Singh, Vikram Singh and Jagmal Singh. 
Pratap also had two stepsisters: Chand Kanwar and Man Kanwar. His chief consort was Ajabde Bai Punwar of Bijolia.[8] Their 
eldest son was Amar Singh I.[9] He belonged to the royal family of Mewar.[10] After the death of Udai Singh in 1572, Rani 
Dheer Bai Bhatiyani wanted her son Jagmal to succeed him[11] but senior courtiers preferred Pratap, as the eldest son, to be their 
king. The desire of the nobles prevailed and Pratap ascended the throne as Maharana Pratap, the 54th ruler of Mewar in the line of 
the Sisodia Rajputs.[12] He was crowned in Gogunda on the auspicious day of Holi. Jagmal swore revenge and left for Ajmer, to join 
the armies of Emperor Akbar. He was given the town of Jahazpur as a Jagir as a gift in return for his help.[13]

Military career:
Background:
Pratap Singh, gained distinction for his refusal to form any political alliance with the Mughal Empire and his resistance to Mughal domination. 
The conflicts between Pratap Singh and Akbar led to the Battle of Haldighati.[14][15]

Battle of Haldighati:
Main article: Battle of Haldighati:
The Siege of Chittorgarh in 1567-1568 had led to the loss of the fertile eastern belt of Mewar to the Mughals. However, the rest of the wooded 
and hilly kingdom in the Aravalli range was still under the control of Maharana Pratap. Mughal Emperor Akbar was intent on securing a stable 
route to Gujarat through Mewar; when Pratap Singh was crowned king (Maharana) in 1572, Akbar sent a number of envoys, including one by Raja 
Man Singh I of Amer, entreating him to become a vassal like many other rulers in Rajputana. When Pratap refused to personally submit to Akbar 
and several attempts to diplomatically settle the issue failed, war became inevitable.[16][17]

The forces of Pratap Singh and Mughal and Rajput general Man Singh met on 18 June 1576 beyond a narrow mountain pass at Haldighati near 
Gogunda, modern day Rajsamand in Rajasthan. This came to be known as the Battle of Haldighati. Pratap Singh fielded a force of around 3000 
cavalry and 400 Bhil archers. Man Singh commanded an army numbering around 10,000 men.[18][19][20] After a fierce battle lasting more than 
three hours, Pratap found himself wounded and the day lost. He managed to retreat to the hills and lived to fight another day.[21] 
The Mughals were victorious and inflicted significant casualties among the forces of Mewar but failed to capture Maharana Pratap.[18][19][20]

Haldighati was a futile victory for the Mughals, as they were unable to kill or capture Pratap, or any of his close family members 
in Udaipur.[22] While the sources also claim that Pratap was able to make a successful escape, Man Singh managed to conquer Gogunda
 within a week after Haldighati then ended his campaign. Subsequently, Akbar himself led a sustained campaign against the Rana in 
 September 1576, and soon, Gogunda, Udaipur, and Kumbhalgarh were all under Mughal control.[22]

Post-Haldighati Mughal invasions:
Shahbaz Khan Kamboh led multiple invasions that resulted in the subjugation of key areas in Mewar, such as Kumbhalgarh, Mandalgarh, 
Gogunda, and Central Mewar, bringing them permanently under Mughal rule. The Mughal Empire established its supremacy in Mewar after 
Shahbaz Khan's invasions. This ultimately led to a significant weakening of Pratap's power, forcing him to retreat to his hilly abode.[23]

Patronage of art:
Maharana Pratap's court at Chavand had given shelter to many poets, artists, writers and artisans. The Chavand school of art was 
developed during the reign of Rana Pratap. He also had renowned artists like Nasiruddin in his court.[24]

Revival of Mewar:
Mughal pressure on Mewar relaxed after 1579 following rebellions in Bengal and Bihar and Mirza Hakim's incursion into the Punjab. 
After this Akbar sent Jagannath Kachhwaha to invade Mewar in 1584. This time too Mewar army defeated Mughals and forced them to 
retreat. In 1585, Akbar moved to Lahore and remained there for the next twelve years watching the situation in the north-west. 
No major Mughal expedition was sent to Mewar during this period.[25] Taking advantage of the situation, Pratap recovered some of 
Mughal occupied areas of Mewar and captured thirty-six Mughal outposts. Udaipur, Mohi, Gogunda, Mandal and Pandwara were some of 
the important areas that were recaptured from this conflict. According to the 1588 inscription near Jahazpur, the Rana gave the 
lands of Pander to a trusted follower called Sadulnath Trivedi. G.N. Sharma claims that the Pander inscription is proof that the 
Rana had occupied north-eastern Mewar and was granting lands to those who had been loyal to him.[25][26] From 1585 till his death, 
the Rana had recovered a large part of Mewar. The citizens who had migrated out of Mewar started returning during this time. 
There was good monsoon which helped to revive the agriculture of Mewar. The economy also started getting better and trade in the area 
started increasing. The Rana was able to capture the territories around Chittor but could not fulfill his dream of capturing Chittor itself.[27]

Death
Reportedly, Pratap died of injuries sustained in a hunting accident,[28] at Chavand[25] on 19 January 1597, aged 56.[29] He was 
succeeded by his eldest son, Amar Singh I. On his death bed, Pratap told his son never to submit to the Mughals and to win Chittor back.[30]

It is said that even Akbar was shocked to hear the news of Maharana Pratap's death. Dursa Arha, the court poet of Akbar, is said to 
have eulogised Maharana Pratap in the Mughal court.[31]
"""

if __name__ == "__main__":
    print("Hello Langchain!")

    print(
        "\n======================================================================================\n"
    )

    load_dotenv()
    # print(os.getenv('OPENAI_API_KEY1'))

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    print(
        f"The type of summary_prompt_template {type(summary_prompt_template)} \nThe Summary Prompt Template variable: {summary_prompt_template}"
    )  # Type: <class 'langchain_core.prompts.prompt.PromptTemplate'>

    print(
        "\n======================================================================================\n"
    )

    # llm = ChatOpenAI(
    #     temperature=0, model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY1")
    # )

    llm = ChatOllama(model="llama3")

    print(
        f"The type of llm: {type(llm)}"
    )  # <class 'langchain_openai.chat_models.base.ChatOpenAI'>

    print(
        "\n======================================================================================\n"
    )

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(
        f"Type of chain: {type(chain)}"
    )  # <class 'langchain_core.runnables.base.RunnableSequence'>

    print(
        "\n======================================================================================\n"
    )

    pprint(
        f"The type of res: {type(res)} \nResult is {res}"
    )  # Type: <class 'langchain_core.messages.ai.AIMessage'>
