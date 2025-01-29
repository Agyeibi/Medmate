from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime
import random
from kivy.uix.popup import Popup



# Define the HealthTips class to manage health tips
class HealthTips:
    def __init__(self):
        self.tips = [
            "Drink enough water every day!",
            "Exercise for at least 30 minutes daily.",
            "Eat a balanced diet with plenty of fruits and vegetables.",
            "Get 7-8 hours of sleep every night.",
            "Wash your hands regularly to avoid germs.",
            "Take breaks to reduce stress throughout the day.",
            "Don't skip breakfast! Start your day with healthy food.",
            "Avoid smoking and excessive alcohol consumption.",
            "Practice good posture to avoid back pain.",
            "Get regular checkups to monitor your health."
        ]
    
    def get_random_tip(self):
        return random.choice(self.tips)


# Define the TipScreen class to display tips
class TipScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.health_tips = HealthTips()  # Initialize the HealthTips class


# Screen Classes
class PageScreen(Screen):
    pass

class NghtScreen(Screen):
    pass

class LoginScreen(Screen):
    def validate_login(self):
        # Example logic for login validation
        email = self.ids.email.text
        password = self.ids.password.text

        if not email or not password:
            print("Email and password cannot be empty.")
        elif "@" not in email:
            print("Invalid email address.")
        else:
            print("Login successful.")
            self.manager.current = "home"

class SignUpScreen(Screen):
    def create_account(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if not email and not password:
            print("All fields are required!")
        elif "@" not in email:
            print("Enter a valid email address!")
        else:
            print("Account created successfully!")
            self.manager.current = "login"

# Define the TelemedScreen class
class TelemedScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add a button to the screen as a test
        btn = Button(text="Welcome to Telemed Screen!")
        self.add_widget(btn)

# Define the main app class
class MedMateApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelemedScreen(name='telemed'))
        return sm
    
class HomeScreen(Screen):
    pass

class ContactUsScreen(Screen):
    pass

class PatientProfileScreen(Screen):
    pass

class EditPatientScreen(Screen):
    pass

class ContactListScreen(Screen):
    pass
class ConversationScreen(Screen):
    def suggest_medicine(self, query):
        print(f"Received query: {query}")
    MEDICINE_SUGGESTIONS = {
        "cold": "Paracetamol, Cough Syrup",
        "fever": "Ibuprofen, Acetaminophen",
        "headache": "Aspirin, Naproxen",
        "stomach ache": "Antacid, Buscopan",
    }

    def suggest_medicine(self, disease_name):
        disease_name = disease_name.lower()
        return self.MEDICINE_SUGGESTIONS.get(disease_name, "Consult a healthcare professional.")

class chatapp1Screen(Screen):
    pass

class ChatScreen(Screen):
    def send_message(self):
        timestamp = datetime.now().strftime("%H:%M")
        chat_input = self.ids.chat_input
        chat_messages = self.ids.chat_messages

        message = chat_input.text
        if message.strip():
            chat_messages.text += f"\nYou: {message}"
            chat_input.text = ""

class Chat2Screen(Screen):
    def send_message(self):
        chat_input = self.ids.chat_input
        chat_messages = self.ids.chat_messages

        message = chat_input.text
        if message.strip():
            chat_messages.text += f"\nYou: {message}"
            chat_input.text = ""

class Chat3Screen(Screen):
    def send_message(self):
        chat_input = self.ids.chat_input
        chat_messages = self.ids.chat_messages

        message = chat_input.text
        if message.strip():
            chat_messages.text += f"\nYou: {message}"
            chat_input.text = ""

class HealthTips:
    def __init__(self):
        self.tips = [
            "Drink enough water every day!",
            "Exercise for at least 30 minutes daily.",
            "Eat a balanced diet with plenty of fruits and vegetables.",
            "Get 7-8 hours of sleep every night.",
            "Wash your hands regularly to avoid germs.",
            "Take breaks to reduce stress throughout the day.",
            "Don't skip breakfast! Start your day with healthy food.",
            "Avoid smoking and excessive alcohol consumption.",
            "Practice good posture to avoid back pain.",
            "Get regular checkups to monitor your health.",
            "Aim for at least 30 minutes of exercise each day.",
            "Get enough sleep to rejuvenate your body.",
            "Eat a balanced diet with lots of fruits and vegetables.",
            "Take breaks and move around to avoid sitting too long.",
            "Practice good posture to avoid back and neck strain.",
            "Take time to relax and manage stress effectively.",
            "Keep your mind sharp with regular mental exercises.",
            "Wash your hands regularly to prevent infections.",
            "Limit screen time to reduce eye strain.",
            "Spend time in nature for mental and physical well-being.",
            "Eat smaller, more frequent meals to maintain energy levels.",
            "Don’t skip breakfast, it’s an important meal for energy.",
            "Avoid excessive sugar to maintain healthy blood sugar levels.",
            "Limit processed foods and focus on whole grains.",
            "Stretch daily to maintain flexibility.",
            "Find an activity you love for regular physical activity.",
            "Practice mindfulness or meditation for mental health.",
            "Listen to your body and rest when needed.",
            "Practice good hygiene habits to avoid illnesses.",
            "Incorporate healthy fats like avocados and nuts into your diet.",
            "Limit alcohol intake for better liver health.",
            "Keep a positive mindset to reduce stress levels.",
            "Avoid smoking to protect your lungs and heart.",
            "Have regular health check-ups with your doctor.",
            "Wear sunscreen to protect your skin from UV damage.",
            "Get fresh air regularly to boost mood and energy.",
            "Try a new physical activity to challenge your body.",
            "Take a walk after meals for better digestion.",
            "Use proper ergonomics at your desk to prevent strain.",
            "Stay consistent with your sleep schedule for better rest.",
            "Eat foods rich in fiber for healthy digestion.",
            "Laugh often; it’s good for your mental and physical health.",
            "Set aside time for self-care and relaxation.",
            "Hydrate with herbal teas for additional health benefits.",
            "Avoid excessive caffeine to prevent energy crashes.",
            "Engage in social activities for improved mental health.",
            "Prioritize mental health just as much as physical health.",
            "Practice deep breathing exercises to reduce stress.",
            "Limit junk food intake to maintain a healthy weight.",
            "Ensure proper hydration, especially after exercise.",
            "Use a foam roller to relieve muscle tightness.",
            "Eat foods rich in antioxidants to support your immune system.",
            "Stay connected with loved ones for emotional well-being.",
            "Switch to healthier cooking methods like baking or grilling.",
            "Manage your time effectively to reduce stress.",
            "Get adequate vitamin D from sunlight or supplements.",
            "Try yoga or Pilates for flexibility and strength.",
            "Avoid eating too late in the evening to improve digestion.",
            "Incorporate probiotics into your diet for gut health.",
            "Maintain a healthy weight through balanced nutrition and exercise.",
            "Practice gratitude daily to boost your mood.",
            "Avoid excessive screen time before bed for better sleep.",
            "Take your vitamins regularly for nutritional support.",
            "Get creative with your workouts to keep them fun.",
            "Track your health habits to stay motivated.",
            "Slow down and savor your meals to prevent overeating.",
            "Avoid self-diagnosing; seek professional medical advice.",
            "Ensure your workspace is well-lit to reduce eye strain.",
            "Be mindful of your posture while sitting or standing.",
            "Engage in regular cardio exercises for heart health.",
            "Be kind to yourself; mental health matters.",
            "Learn something new to keep your mind engaged.",
            "Consume healthy snacks like fruits, nuts, or yogurt.",
            "Try to avoid processed sugars and opt for natural sweeteners.",
            "Boost immunity with vitamin-rich foods like citrus fruits.",
            "Limit screen time to improve focus and sleep.",
            "Practice mindfulness while eating to prevent overeating.",
            "Incorporate strength training into your fitness routine.",
            "Check in with your emotions regularly to maintain mental health.",
            "Switch to plant-based meals a few times a week for health benefits.",
            "Stay active throughout the day, even with small movements.",
            "Avoid unhealthy dieting trends and focus on balance.",
            "Find a fitness routine that works for your lifestyle.",
            "Include a variety of colors in your diet for a wider range of nutrients.",
            "Be mindful of portion sizes to avoid overeating.",
            "Spend time doing activities that bring you joy.",
            "Regularly engage in stretching or mobility exercises.",
            "Practice self-compassion and take care of your emotional needs.",
            "Stay hydrated with water and herbal teas, not sugary drinks.",
            "Take time for hobbies or creative outlets for mental wellness.",
            "Make sleep a priority for better physical and mental health.",
            "Stay mindful of your breathing to reduce anxiety.",
            "Incorporate more plant-based meals for overall wellness.",
            "Celebrate your progress and achievements, no matter how small.",
            "Stay motivated by setting small, achievable health goals.",
            "Don’t forget to laugh; it’s great for reducing stress.",
            "Create a positive and inspiring environment at home.",
            "Challenge yourself to try something new each week."

        ]
    
    def get_random_tip(self):
        return random.choice(self.tips)


# Define the TipScreen class to display tips
class TipScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.health_tips = HealthTips()  # Initialize the HealthTips class
        self.label = Label(text=self.health_tips.get_random_tip(), size_hint_y=None, height=44)
        self.add_widget(self.label)

        # Add button to get a new tip
        button = Button(text="Get New Tip", on_press=self.update_tip)
        self.add_widget(button)

    def update_tip(self, instance):
        # Update the label with a new random health tip
        self.label.text = self.health_tips.get_random_tip()





class MedMateApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PageScreen(name="page"))
        sm.add_widget(NghtScreen(name="nun"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignUpScreen(name="signup"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(PatientProfileScreen(name="patientprofile"))
        sm.add_widget(EditPatientScreen(name="editpatient"))        
        sm.add_widget(ContactListScreen(name="contact_list"))
        sm.add_widget(ConversationScreen(name="conversation"))
        sm.add_widget(ChatScreen(name="chat"))  # Add the ChatScreen here
        sm.add_widget(Chat2Screen(name="chat2"))
        sm.add_widget(Chat3Screen(name="chat3"))
        sm.add_widget(TipScreen(name="tip"))

        
        Clock.schedule_once(self.show_tip_popup, 0.5)
        return sm

    def show_tip_popup(self, *args):
        # Show the popup with a health tip
        health_tips = HealthTips()
        tip = health_tips.get_random_tip()
        
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=tip, size_hint_y=None, height=44))
        close_button = Button(text="Thanks", size_hint_y=None, height=44)
        close_button.bind(on_press=self.close_popup)
        content.add_widget(close_button)

        self.popup = Popup(title="Health Tip", content=content, size_hint=(0.8, 0.4))
        self.popup.open()

    def close_popup(self, instance):
        # Close the popup
        self.popup.dismiss()

    def update_health_tip(self):
        # Method to update the health tip
        print("Health Tip updated!")
        # You can add logic to change or refresh the tip if desired

# Run the App
if __name__ == "__main__":
    MedMateApp().run()
