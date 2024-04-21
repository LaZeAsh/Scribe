"""The home page of the app."""

from scribe1 import styles
from scribe1.templates import template
from scribe1.components.geminiComponent import scribeGenerator

import reflex as rx

class LoginState(rx.State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        text_scribe = """
    [doctor] hi joyce, how are you?
    [patient] i'm good. how are you?
    [doctor] i'm doing well. so, I know the nurse told you about dax. i'd like to tell dax a little bit about you when we get started, okay?
    [patient] okay.
    [doctor] all right. so, joyce is a 50 year old female with a past medical history significant for copd, congestive heart failure who presents for follow-up to an abnormal lab finding. so, joyce, i, i got the results of your lab, uh, your labs. your hemoglobin was low. uh, so, i asked them to schedule a follow-up appointment with me. so, how are you feeling?
    [patient] i've been feeling really tired lately. over the past couple of months, i've noticed that my energy has really gone down. i used to be really active, um, just trying to be as healthy as i can be, running, climbing. um, i at least try to do an hour or two a day. and over the past month, it's gone slowly downhill. i've just been so tired and exhausted and i haven't been able to really keep up with the way i, i was g- was going with my exercise.
    [doctor] okay. all right. um, now, have you had... have you noticed any blood in your stools at all?
    [patient] uh, no, not really. not, not at this time.
    [doctor] okay. and are your stools, like, dark or charry or black looking?
    [patient] no. not that i've noticed.
    [doctor] okay. and are you spotting a lot with your periods?
    [patient] no, i'm not.
    [doctor] okay. all right. um, and do you have any other... i know that you are endorsing this fatigue and you feel kind of dizzy and that type of thing. do you have any other symptoms like chest pain, shortness of breath, fever, chills, body aches, anything?
    [patient] no, nothing like that.
    [doctor] okay. any weight loss?
    [patient] um, i've noticed a little bit, but that's because i think i've been doing really well with my exercise. um, but nothing too significant.
    [doctor] okay. all right. well, let me ask you a little bit about how's the, the copd doing. i, i know that, you know, you've stopped smoking several years ago, but, you know, you still have that em- those emphysema changes on your chest x-ray. so, how are you doing with that? how's your breathing?
    [patient] it's been okay. um, i haven't been smoking. i... after i quit, i quit cold turkey and i haven't gone back since. so, that's been doing well. i think, uh, during the changes of season, it gets a little bit harder for me to breathe, but i think that's just because of my allergies.
    [doctor] okay. all right. and then from a congestive heart failure standpoint, are you watching your diet, you're watching your salt intake?
    [patient] yeah. i've been doing really well with that. i've been staying away from the french fries, and all the other salty foods that i love to eat, uh, and everything looks great.
    [doctor] um, so, french fries are one of my favorite foods, that and fried chicken, so-
    [doctor] i give you a lot of credit for staying away from french fries.
    [patient] thank you.
    [doctor] um, okay. so, you... so, no swelling in your legs or any- anything like that.
    [patient] no, not that i've noticed.
    [doctor] okay. and you feel like you have a good support system?
    [patient] yeah. my boyfriend is, is great and i have, um, my brother right down the road.
    [doctor] okay. all right. good. i'm glad to hear that. uh, so, let's go ahead. i wanna just do a quick physical exam, okay?
    [patient] okay.
    [doctor] hey, dragon, show me the vital signs. all right. well, your vital signs here in the office look good, so, i'm, i'm really happy to see that with the abnormal hemoglobin that we saw. um, i'm gonna just listen to your heart and lungs and press on your belly a little bit and i'll let you know if i find anything, okay?
    [patient] okay.
    [doctor] all right. okay. all right. so, on physical exam, you know, i, i don't appreciate anything cervical lymphadenopathy. your heart sounds really good, but i do hear a, a slight two out of six systolic heart, uh, murmur, um, systolic ejection murmur on your heart exam. your lungs sound clear. your abdomen... you know, you did have a little tenderness to palpation in your right lower quadrant on your abdominal exam, uh, but i don't appreciate any lower extremity edema. so, all that means it that we, you know, we hear that heart murmur, which we heard in the past, um, and your belly had some tenderness, so we'll have to talk about that a little bit, uh, going forward, okay?
    [patient] okay.
    [doctor] let's look at some of your results, okay?
    [patient] mm-hmm.
    [doctor] hey, dragon, show me the hemoglobin. so, here, looking at this, you know, your hemoglobin level is 8.2. somebody like you should have a hemoglobin o- of about 13, 14, okay?
    [patient] okay.
    [doctor] so, we need to investigate why it's low. hey, dragon, show me the anemia labs. okay. so, looking here at your labs, uh, everything looks good from, from this standpoint. i think some of your anemia labs are still pending at this time that's part of the workup.
    [patient] mm-hmm.
    [doctor] so, let's go over a little bit about the assessment and plan for you. so, you know, your main problem, this abnormal lab, this low hemoglobin that we found, so, you're anemic and we nee-... you know, i'm waiting for those anemia labs to come back to find out exactly, you know, what type of anemia you have. i'd like to go ahead and schedule you for an endoscopy a- and a colonoscopy just to make sure that you're not bleeding from your, inside your belly, okay? um, and i'm... i'll be in touch when those labs come back to see what further workup we need to do, okay?
    [patient] mm-hmm.
    [doctor] for your next problem, the copd, i think you're doing great. you know, i, i don't think that you, uh, need any further referrals at this time for that. i would just continue staying away from smoking. it doesn't sound to be like you need any inhalers at this time. uh, for your third problem, your congestive heart failure, you know, i wanna continue you on the toprol, continue you on the lisinopril and we'll continue you on your current diuretic dosing of 20, lasix 20 milligrams a day.
    [doctor] i'm gonna go ahead and order that referral to g- to gastroenterology. they're the ones who will do the endoscopy and the colonoscopy, okay?
    [patient] okay.
    [doctor] hey, dragon, order the referral to gastroenterology. so, i'll be in touch. i'm gonna stay in close contact with you over the next week or so and, uh, we'll get this all sorted out, okay?
    [patient] okay.
    [doctor] all right. take care, joyce.
    [patient] thank you.
    [doctor] hey, dragon, finalize the note.
    """

        """Handle the form submit."""
        self.form_data = form_data
        scribeGenerator1=scribeGenerator
        scribeGenerator(text_scribe)
        return rx.redirect("/profile/1")
    

@rx.page(route="/", title="Home")
def index() -> rx.Component:
    return rx.vstack(
        
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    name="username",
                ),
                rx.input(
                    placeholder="Password",
                    name="password",
                ),
                rx.button("Submit", type="submit"),
            ),
            
            on_submit=LoginState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(LoginState.form_data.to_string()),
        )
        
    


    """The home page.

    Returns:
        The UI for the home page.
    """
    # with open("README.md", encoding="utf-8") as readme:
    #     content = readme.read()
    # return rx.markdown(content, component_map=styles.markdown_style)

