from datetime import datetime
from django.views.generic import TemplateView



# Create your views here.
class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context = {
                'time_now': datetime.now(),
                'user': self.request.user.username,
            }

            return context

        context = {
            'time_now': datetime.now(),
        }

        return context

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']

        else:
            return ['common/index.html']



def display_asmb_sofia_info(request):
    context = {
        'asmb_sofia_info': {
            "title": "The Association of Medical Students in Bulgaria – Sofia (AMSB-Sofia)",
            "description": (
                "The Association of Medical Students in Bulgaria – Sofia (AMSB-Sofia) is a voluntary non-governmental "
                "organization working in the interest of medical students at Sofia Medical University. AMSB-Sofia represents "
                "more than 1000 medical students. Since its establishment on September 30, 2003, the Association has made "
                "significant progress, and it is currently an active member of the Bulgarian Association of Medical Students (BAMS), "
                "the International Federation of Medical Students’ Associations (IFMSA), and the European Medical Students’ Association (EMSA)."
            ),
            "goals": (
                "One of the main goals is to unite medical students and enhance their professional qualifications. AMSB-Sofia also organizes "
                "a large number of campaigns and projects related to the prevention and awareness of socially significant diseases such as "
                "diabetes, hypertension, HIV/AIDS, and others."
            ),
            "projects": (
                "The Association's projects are also focused on society – increasing medical awareness, enriching knowledge about socially "
                "significant diseases, and methods of prevention. These projects are prepared and implemented by medical students, members "
                "of AMSB-Sofia. This is a process of knowledge exchange and experience between medical students and the society, which is "
                "both enjoyable and beneficial for both parties."
            ),
            "membership": (
                "AMSB-Sofia provides an opportunity for students to engage in various educational, social, and professional activities "
                "related to the medical field. Members contribute to organizing public health campaigns, workshops, and other social events."
            ),
            "affiliations": [
                "Bulgarian Association of Medical Students (BAMS).",
                "International Federation of Medical Students’ Associations (IFMSA).",
                "European Medical Students’ Association (EMSA)."
            ],
            "benefits": (
                "Becoming a member of AMSB-Sofia offers opportunities to engage in meaningful projects, enhance professional skills, "
                "and make lasting connections with like-minded individuals and organizations."
            )
        }
    }

    return render(request, 'branches/asmb_sofia_description.html', context)


def display_asmb_varna_info(request):
    context = {
        'asmb_varna_info': {
            "title": "The Association of Medical Students in Bulgaria – Varna (AMS – Varna)",
            "description": (
                "AMS – Varna is a voluntary non-governmental organization. Its goal is to unite students from the 'Medicine' "
                "program at the Medical University 'Prof. Dr. Paraskev Stoyanov' – Varna, by developing their practical skills "
                "and academic knowledge. AMS-Varna represents the opinions and interests of medical students across the country "
                "as a full member of the Association of Medical Students in Bulgaria (AMSB) and on global issues through the "
                "International Federation of Medical Students' Associations (IFMSA)."
            ),
            "history": (
                "AMS-Varna was founded on June 9, 2005, and has been continuously evolving ever since. Today, its members number over 500."
            ),
            "goals": (
                "The association unites medical students in Varna by organizing various campaigns, including informational, "
                "charitable, and screening events, as well as lectures and workshops aimed at enhancing students' practical skills."
            ),
            "collaborations": (
                "AMS-Varna conducts its events independently or in collaboration with other governmental and non-governmental organizations, "
                "such as Varna Municipality, the Directorate for Prevention, the National Alliance for People with Rare Diseases, "
                "the 'Pituitary Association,' and many others. It works closely with the Medical University – Varna, its Student Council, "
                "UMHAT 'St. Marina,' the Association of Dental Medicine Students in Varna (ADMS-Varna), and the Association of Pharmacy Students "
                "in Varna (APSV)."
            ),
            "impact": (
                "Through this collaboration, the association successfully reaches the citizens of the city. This is not only interesting and enjoyable "
                "for students but also beneficial for people, helping them learn more about their health and how to care for it."
            ),
            "international_exchange": (
                "AMS-Varna, along with AMS-Sofia, AMS-SU, AMS-Plovdiv, AMS-Pleven, AMS-Stara Zagora, and AMS-Burgas, participates in the international student "
                "exchange program organized by IFMSA. Every year, it welcomes and sends students eager to explore different cultures and innovative methods of "
                "diagnosis and treatment."
            )
        }
    }

    return render(request, 'branches/asmb_varna_description.html', context)


def display_asmb_pleven_info(request):
    context = {
        'asmb_pleven_info': {
            "title": "The Association of Medical Students in Bulgaria – Pleven (ASMB-Pleven)",
            "description": (
                "ASMB-Pleven is an autonomous, independent, apolitical, non-governmental organization of medical students in Bulgaria. "
                "It is a non-profit organization and a legal entity. ASMB-Pleven is part of the Association of Medical Students in Bulgaria (ASMB) "
                "and the International Federation of Medical Students' Associations (IFMSA). The association collaborates with the Medical University of Pleven, "
                "the Student Council at the Medical University of Pleven, University Hospital 'Dr. Georgi Stranski', the Municipality of Pleven, and other local NGOs such as "
                "the National Alliance of People with Rare Diseases, the Regional Health Inspectorate, among others."
            ),
            "goals": (
                "The main goals of ASMB-Pleven are:"
                "<ul>"
                "<li>Uniting medical students irrespective of political, religious, and national affiliation to democratize the educational process in higher education institutions.</li>"
                "<li>Enhancing professional qualifications and elevating the social status of medical students.</li>"
                "<li>Exchanging information and addressing issues in medical education by analyzing, summarizing, and publicizing these problems while coordinating efforts to solve them.</li>"
                "<li>Organizing international student exchanges.</li>"
                "<li>Representing medical students’ social concerns to governmental bodies and public organizations, advocating for solutions.</li>"
                "<li>Protecting the rights and legitimate interests of medical students.</li>"
                "<li>Promoting public health, improving the status of disadvantaged individuals through campaigns and charitable initiatives.</li>"
                "</ul>"
            ),
            "activities": (
                "Over the years, ASMB-Pleven has organized numerous campaigns and seminars aimed at public health, charity, and the interests of medical students. Examples include:"
                "<ul>"
                "<li>Campaigns for World Heart Day</li>"
                "<li>Campaigns for World Diabetes Day</li>"
                "<li>Campaigns for World AIDS Day</li>"
                "<li>Christmas and Slavic Literacy Day charity campaigns, collecting toys, clothes, and books</li>"
                "<li>Seminars on Rare Diseases</li>"
                "<li>Modern Obstetrics and Gynecology School</li>"
                "<li>Oncology Seminars</li>"
                "<li>Campaigns for World Tuberculosis Day</li>"
                "<li>Campaigns for World Asthma Day</li>"
                "<li>Campaigns to prevent smoking</li>"
                "<li>Peace March 'Speak Up, Someone Will Hear You', against violence towards women</li>"
                "<li>'Thank You, Doctor' Campaign</li>"
                "<li>'Teddy Bear Hospital' Initiative</li>"
                "<li>Lectures on the occasion of World Sleep Day</li>"
                "<li>Nations Party</li>"
                "<li>Observance of the Day for the Elimination of Racial Discrimination</li>"
                "<li>Annual exchange programs</li>"
                "<li>Many others</li>"
                "</ul>"
            ),
            "structure": (
                "The organization is managed by a Management Board and supervised by a Control Board. "
                "The Management Board includes roles such as Chairperson, Vice-Chairperson, Secretary, and PR, along with several committees, each with a designated head:"
            ),
            "committees": [
                "Medical Education",
                "Public Health",
                "Reproductive Health and AIDS",
                "Professional Exchange",
                "Scientific Exchange",
                "Human Rights and Peace",
                "International Projects and Relations with English-Speaking Students"
            ],
            "control_board": (
                "The activities of ASMB-Pleven are overseen by the Control Board, consisting of a three-member commission."
            ),
        }
    }

    return render(request, 'branches/asmb_pleven_description.html', context)



def display_asmb_burgas_info(request):
    context = {
        'asmb_burgas_info': {
            "title": "The Association of Medical Students in Bulgaria – Burgas (ASMB-Burgas)",
            "description": (
                "ASMB-Burgas is a non-governmental, non-political, and non-religious organization comprising medical students from the Medical Faculty "
                "of Prof. Dr. Assen Zlatarov University, Burgas. Established in December 2021, the association currently has 44 medical student members "
                "from all academic years. ASMB-Burgas is part of the Association of Medical Students in Bulgaria (ASMB), which is affiliated with the "
                "International Federation of Medical Students' Associations (IFMSA)."
            ),
            "objectives": (
                "The main objectives of ASMB-Burgas are:"
                "<ul>"
                "<li>Unite medical students.</li>"
                "<li>Enhance their professional qualifications.</li>"
                "<li>Elevate the social status of medical students.</li>"
                "<li>Exchange information, analyze, summarize, and publicize issues related to medical education and coordinate efforts to address them.</li>"
                "<li>Organize and conduct public campaigns on socially significant topics.</li>"
                "<li>Facilitate international student exchange programs.</li>"
                "<li>Defend the rights and legitimate interests of medical students.</li>"
                "<li>Provide comprehensive support for personal and collective initiatives of medical students.</li>"
                "</ul>"
            ),
            "partnerships": (
                "Since its establishment, ASMB-Burgas has successfully partnered with the Municipality of Burgas and continues to build relationships "
                "with local organizations and institutions."
            ),
            "structure_and_committees": (
                "The association is organized into six areas of focus, represented by specific committees:"
            ),
            "committees": [
                "Medical Education",
                "Reproductive Health and AIDS",
                "Public Health",
                "Human Rights and Peace",
                "Scientific Exchange",
                "Professional Exchange"
            ],
            "committee_focus": (
                "The Medical Education, Reproductive Health and AIDS, Public Health, and Human Rights and Peace committees focus on organizing and conducting public awareness campaigns. "
                "The Scientific Exchange and Professional Exchange committees manage international internships."
            ),
        }
    }

    return render(request, 'branches/asmb_burgas_description.html', context)



from django.shortcuts import render

def display_asmb_stara_zagora_info(request):
    context = {
        'asmb_stara_zagora_info': {
            "title": "The Association of Medical Students in Bulgaria – Stara Zagora (ASMB – Stara Zagora)",
            "description": (
                "ASMB – Stara Zagora is a voluntary, independent, and non-political organization of medical students with a non-profit purpose. "
                "It is a member of the Association of Medical Students in Bulgaria (ASMB), the International Federation of Medical Students' Associations (IFMSA), "
                "and the European Medical Students Association (EMSA)."
            ),
            "history": (
                "Established on February 29, 2000, its members are medical students studying at the Medical Faculty of Trakia University in Stara Zagora."
            ),
            "management_structure": (
                "The ASMB – Stara Zagora management board consists of a Chairperson, Vice-Chairperson, Secretary, and a Public Relations Officer (PR). "
                "The organization operates through several committees, each working in close collaboration with the others:"
            ),
            "committees": [
                "Medical Education",
                "Public Health",
                "Reproductive Health",
                "Professional Exchange",
                "Scientific Exchange",
                "Human Rights and Peace"
            ],
            "objectives": (
                "The main objectives of ASMB – Stara Zagora are:"
                "<ul>"
                "<li>Unite medical students, regardless of their political, religious, or national affiliations, to democratize the educational process in higher education institutions.</li>"
                "<li>Enhance the professional qualifications and social status of medical students in line with international standards, continuously updating these standards.</li>"
                "<li>Facilitate the exchange of information, analyze, summarize, and publicize issues related to education in higher institutions, and coordinate efforts to resolve them.</li>"
                "<li>Represent educational and social issues of medical students to relevant state and public bodies and organizations, advocating for their resolution.</li>"
                "<li>Defend and uphold the rights and interests of medical students, as guaranteed by the Constitution of Bulgaria, laws, and international agreements signed by Bulgaria.</li>"
                "</ul>"
            ),
            "activities": (
                "In recent years, ASMB – Stara Zagora and its members have successfully organized various campaigns, including:"
                "<ul>"
                "<li>Teddy Bear Hospital: A campaign where children's toys are given a 'medical check-up' to demonstrate that visiting the doctor is not something to fear.</li>"
                "<li>Anti-AIDS Campaign: Focused primarily on the prevention of sexually transmitted diseases.</li>"
                "<li>Informative lectures: Featuring specialists from various fields of medicine and competitions aimed at raising awareness of specific issues, sparking public interest, and many other activities.</li>"
                "</ul>"
            ),
        }
    }

    return render(request, 'branches/asmb_stara_zagora_description.html', context)





class ASMPlovdivView(TemplateView):
    template_name = "branches/asm_plovdiv.html"  # Replace with the actual template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asm_plovdiv_info'] = {
            "title": "Association of Medical Students – Plovdiv (ASM-Plovdiv)",
            "description": (
                "The Association of Medical Students – Plovdiv (ASM-Plovdiv) is an organization "
                "dedicated to uniting medical students from the Medical University – Plovdiv. Established "
                "on March 10, 2002, it currently has over 450 members, including students from all years of study at "
                "the university, as well as practicing physicians who are alumni."
            ),
            "activities": [
                "Public Health Campaigns addressing issues like hypertension, tuberculosis, COPD, and rare diseases.",
                "Campaigns promoting Reproductive Health and HIV/AIDS awareness.",
                "Human Rights initiatives, charity campaigns, and other public events.",
                "Defends and advocates for the rights of medical students during their education.",
                "Exchange internships (1-month programs) with universities abroad.",
                "Organizes international conferences.",
                "Participates in national and international medical forums and conferences.",
                "Implements EU youth projects."
            ],
            "membership": (
                "Any medical student at the Medical University – Plovdiv is eligible to become a member of ASM-Plovdiv. "
                "New members are admitted by submitting a written application to the ASM-Plovdiv Management Board. "
                "Application forms are available at the association's weekly meetings or from any board member."
            ),
            "affiliations": [
                "The Association of Medical Students in Bulgaria (ASMB).",
                "The European Medical Students’ Association (EMSA).",
                "The International Federation of Medical Students’ Associations (IFMSA)."
            ],
            "benefits": (
                "Apart from its professional and academic value, membership in ASM-Plovdiv offers unforgettable experiences "
                "and the opportunity to meet many new friends, fostering a sense of community and camaraderie."
            )
        }
        return context

def display_asmb_sofia_university_info(request):
    context = {
        'asmb_sofia_university_info': {
            "title": "The Association of Medical Students in Bulgaria – Sofia University (ASMB-Sofia University)",
            "description": (
                "We are a young organization founded in 2010, based in the Medical Faculty of Sofia University. Our members are future doctors united by the idea of effective healthcare, prevention, and health promotion among society."
            ),
            "structure": (
                "The organization consists of three main structures – the Management Board, the Control Board, and the Committees."
                " The Management Board includes:"
                "<ul>"
                "<li>Presidency Board</li>"
                "<li>President</li>"
                "<li>Vice President</li>"
                "<li>Administrative-Financial Officer</li>"
                "<li>Public Relations Officer</li>"
                "<li>Committee Leaders:</li>"
                "<ul>"
                "<li>Public Health</li>"
                "<li>Reproductive Health</li>"
                "<li>Human Rights and Peace</li>"
                "<li>Medical Education</li>"
                "<li>Scientific Exchange</li>"
                "<li>Professional Exchange</li>"
                "</ul>"
                "</ul>"
            ),
            "activities_focus": (
                "Our activities focus mainly on two areas:"
                "<ul>"
                "<li>Developing knowledge and skills of medical students.</li>"
                "<li>Improving public health.</li>"
                "</ul>"
                "The association's work aims to address the needs of young medical students regarding medical education – enhancing the quality and expanding the scope of the training. ASMB-Sofia University strives to contribute to the creation of new opportunities for the future career development of medical professionals."
                "In the healthcare sector, we are guided by the need for health prevention and health promotion. We carry out a combination of medical and non-medical initiatives to achieve better health and quality of life. Our focus is on raising awareness about risk factors, the need for disease prevention, and improving the quality of life by reducing health consequences."
            ),
            "how_we_work": (
                "Practice is an essential need for medical students. Our association prioritizes hands-on practice alongside experienced doctors, providing opportunities for extracurricular activities, such as experimental work in laboratory settings."
                "We also offer Bulgarian students the chance to experience foreign work environments and exchange knowledge with peers from around the world. We all understand the need for better education, and we aim to collaborate with state institutions in this regard."
            ),
            "health_campaigns": (
                "Our health campaigns, programs, and initiatives are carried out at various intervals, often on a specific day with repeated activities in the scheduled programs or initiatives. The campaigns aim to directly reach the Bulgarian public and accomplish the goals of a specific program."
                "Campaigns are grouped into three categories:"
                "<ul>"
                "<li>Informational – to alert society about the existence of a health issue.</li>"
                "<li>Educational – to provide knowledge and techniques for a target group to address a particular problem.</li>"
                "<li>Prevention – offering medical care at the campaign site or providing free medical consultations with specialists.</li>"
                "</ul>"
                "Health initiatives reflect our understanding of healthcare in Bulgaria and our position on it. The primary goal of these initiatives is to present the association's stance on a particular social issue, showing the current situation from an overview perspective and our vision for the future."
            ),
            "scientific_conferences": (
                "In this age of advanced communication, medical students exchange experience and knowledge by organizing international and national scientific conferences on various topics. Such youth organizations improve communication between future colleagues, allowing them to present their own research or collaborate in scientific teams."
            ),
            "annual_activities": {
                "informational_campaigns": [
                    "Sports Day – May 30",
                    "Training on 'Peers Educating Peers'",
                    "World AIDS Day",
                    "FACT: HIV, AIDS. DON’T BECOME A STATISTIC – 2013",
                    "High Blood Pressure Prevention",
                    "Diabetes Screening",
                    "'Together at Easter' – Visiting children in orphanages",
                    "'Together in Diversity' – World Day Against Homophobia"
                ],
                "practical_training": [
                    "Winter Surgery Academy",
                    "SUMMER EMERGENCY MEDICINE ACADEMY",
                    "First Aid Training"
                ],
                "seminars": [
                    "One-Day Seminar – 'Homeopathy and Other Alternative Treatments'",
                    "Seminar on 'Cancerogenesis – Modern Hypotheses'",
                    "Team Building and Seminar on 'Emergency Therapy and Management of Mass Casualty Incidents'",
                    "Seminar 'Stem Cell Transplantation'"
                ]
            }
        }
    }

    return render(request, 'branches/asmb_sofia_university_description.html', context)
