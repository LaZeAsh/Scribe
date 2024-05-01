"""The dashboard page."""

from scribe1.templates import template
from scribe1.components.visit import visitLink
from scribe1.components.alerts import alerts
from scribe1.components.sidebar import sidebar
from scribe1.components.audioRecorder import audioIndex
import reflex as rx
from scribe1.pages.patientData import testData
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


class DynamicFormState(rx.State):    
    
    @rx.var
    def getPatientID(self) -> str:
        return self.router.page.params.get("patientID", "no patientID")
    
    # patient_info = testData.get(self.router.page.params.get("patientID"))

    # if patient_info:
    #     # Extract the required details
    #     info1 = patient_info[0]['patientInfo1']
    #     info2 = patient_info[0]['patientInfo2']
    #     info3 = patient_info[0]['patientInfo3']
        
        # Prepare the formatted data
        # section1_fields: list[list[str]] = [
        #     [{"first_name": info1.get('firstName', "")}, {"middle_name": info1.get('middleName', "")}, {"last_name": info1.get('lastName', "")}],
        #     [{"address": info2.get('Address', "")}, {"city": info2.get('City', "")}, {"state": info2.get('State', "")}, {"zip": info2.get('Zip', "")}],
        #     [{"social_security": info3.get('socialSecurity', "")}, {"age": info3.get('age', "")}, {"sex": info3.get('sex', "")}]
        # ]

    

    

    section1_fields: list[list[str]] = [["first_name", "middle_name","last_name"],
    ["address","city", "state", "zip"], ["social_security","age", "sex"]]
    section2_fields: list[str] = ["past_conditions", "surgical_procedures","allergies", "antecedents"]
    section3_fields: list[list[str]] = [["Medication1", "Dosage1", "Frequency1"],["Medication2", "Dosage2", "Frequency2"],["Medication3", "Dosage3", "Frequency3"]]

    section3_table_data: list[list[str]] = [
        ["","" , ""],
        ["","" , ""],
        ["","" , ""],
        ["","" , ""],
        ["","" , ""],
    ]
    section4_visits: list[str] = ["4/1/23", "8/7/23"]
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        print(form_data)
        self.form_data = form_data

        try:
            model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")
            tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")

            prompt = f"Given that the person is {self.form_data['age']} years old, is a {self.form_data['sex']}, and is taking {self.form_data['Medication1']} at {self.form_data['Dosage1']} {self.form_data['Frequency1']}, what is the likely diagnosis?"
            input_ids = tokenizer.encode(prompt, return_tensors='pt')

            output = model.generate(input_ids, max_length=50, num_return_sequences=1, num_beams=5, early_stopping=True)
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
            print("generating")
            print(generated_text)

        except Exception as e:
            print(f"An error occurred: {str(e)}")



# @template(route="/dashboard", title="Dashboard")
@template(route="/profile/[patientID]", title="patient")
def dashboard() -> rx.Component:
    patientID = DynamicFormState.getPatientID

    # return rx.chakra.form(
    #     rx.chakra.input(name="input1"),
    #     rx.chakra.button("submit", type="submit"),
    #     on_submit=DynamicFormState.handle_submit
    # )
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.chakra.form(
                rx.card(
                    # rx.heading(patientName, size='9')
                    rx.heading("Section I. Patient Information"),
                        rx.vstack(
                            rx.foreach(
                                DynamicFormState.section1_fields,
                                lambda fields_group, idx: rx.chakra.hstack(
                                    rx.foreach(
                                        fields_group,
                                        lambda field, idx: rx.chakra.form_control(
                                            rx.chakra.form_label(field, html_for=field),
                                            rx.chakra.input(placeholder="Enter your " + field, name=field),
                                            is_required=True
                                        )
                                    ) 
                                ),
                            ),
                        ),
                    size="5", 
                    width="100%"
                ),
                rx.card(
                    rx.heading("Section II. Medical History"),
                        rx.vstack(
                            rx.foreach(
                                DynamicFormState.section2_fields,  
                                lambda field, idx: rx.chakra.form_control(
                                    rx.chakra.form_label(field, html_for=field),
                                    rx.text_area(placeholder="Enter your " + field),
                                    is_required=True
                                        
                                ),
                            ),
                        ),
                    size="5", 
                    width="100%"
                ),
                rx.card(
                    rx.heading("Section III. Current Medications"),
                        rx.vstack(
                            rx.foreach(
                                DynamicFormState.section3_fields,
                                lambda fields_group, idx: rx.chakra.hstack(
                                    rx.foreach(
                                        fields_group,
                                        lambda field, idx: rx.chakra.form_control(
                                            rx.chakra.form_label(field, html_for=field),
                                            rx.chakra.input(placeholder="Enter " + field, name=field),
                                            is_required=True
                                        )
                                    ) 
                                ),
                            ),
                        ),
                    size="5", 
                    width="100%"
                ),
                rx.card(
                    rx.heading("Section IV. Visit History"),
                        rx.vstack(
                            rx.hstack(
                                rx.popover.root(
                                    rx.popover.trigger(
                                        rx.button("Add a visit", variant="classic"),
                                    ),
                                    rx.popover.content(
                                        rx.box(
                                            rx.hstack(
                                                rx.input(
                                                    placeholder="MM/DD/YYYY",
                                                ),
                                                rx.popover.close(
                                                    rx.button("Add", size="1")
                                                ),
                                            ),
                                            padding_top="12px",
                                        ),
                                        style={"width": 360},
                                    ),
                                ),
                                rx.popover.root(
                                    rx.popover.trigger(
                                        rx.button("Record a visit", variant="classic"),
                                    ),
                                    rx.popover.content(
                                        rx.box(
                                            rx.hstack(
                                                audioIndex(),
                                                rx.popover.close(
                                                    rx.button("Done", size="1")
                                                ),
                                            ),
                                            padding_top="12px",
                                        ),
                                        style={"width": 360},
                                    ),
                                ),
                            ),
                            rx.foreach(
                                DynamicFormState.section4_visits,
                                lambda visit, idx:
                                visitLink(visit) 
                            )
                        ),
                    size="5", 
                    width="100%"
                ),
                rx.button("Submit", type="submit"),
                on_submit=DynamicFormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.text(DynamicFormState.form_data.to_string()),
            spacing="2",
            align_items="flex-start",
            flex_wrap="wrap",
            # width="100%",
        ),
        alerts(),
        
)