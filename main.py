from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from PIL import Image as PilImage
import os
import sys

class KareemRepairApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # عنوان التطبيق
        self.title_lbl = Label(
            text="Kareem Repair - إصلاح الوسائط والملفات المخفية", 
            font_size='18sp',
            size_hint=(1, 0.1),
            halign='center'
        )
        
        # صندوق لعرض نتائج الفحص والإصلاح
        self.result_lbl = Label(
            text="جاهز للعمل... اضغط على الزر أدناه لبدء فحص الملفات.",
            font_size='14sp',
            halign='center',
            valign='top'
        )
        self.result_lbl.bind(size=self.result_lbl.setter('text_size'))
        
        scroll = ScrollView(size_hint=(1, 0.6))
        scroll.add_widget(self.result_lbl)
        
        # أزرار التحكم
        btn_fix_hidden = Button(
            text="فحص وإصلاح الملفات والصور المخفية", 
            size_hint=(1, 0.15),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        btn_fix_hidden.bind(on_press=self.fix_hidden_files)
        
        btn_test_pillow = Button(
            text="فحص مكتبة معالجة الصور (Pillow)", 
            size_hint=(1, 0.15),
            background_color=(0.2, 0.7, 0.3, 1)
        )
        btn_test_pillow.bind(on_press=self.test_pillow)
        
        layout.add_widget(self.title_lbl)
        layout.add_widget(scroll)
        layout.add_widget(btn_fix_hidden)
        layout.add_widget(btn_test_pillow)
        
        return layout

    def fix_hidden_files(self, instance):
        try:
            # تحديد مسار التخزين (يمكن تخصيصه لبطاقة الذاكرة الخارجية أو المسار الحالي)
            target_path = "/storage/emulated/0/" if os.path.exists("/storage/emulated/0/") else os.getcwd()
            
            fixed_count = 0
            scanned_count = 0
            
            self.result_lbl.text = f"جاري فحص المسار:\n{target_path}\nيرجى الانتظار..."
            
            # حلقة لفحص الملفات وإزالة خاصية الإخفاء للملفات التي تبدأ بنقطة أو المجلدات الشبيهة بـ DCIM
            for root, dirs, files in os.walk(target_path):
                # تحديد الحد الأقصى لتجنب إبطاء التطبيق بالكامل في الذاكرة الداخلية الكبيرة
                if scanned_count > 2000:
                    break
                    
                for file in files:
                    scanned_count += 1
                    file_path = os.path.join(root, file)
                    
                    # إذا كان الملف مخفياً أو يبدأ بنقطة (مشكلة نقل الذاكرة الشائعة)
                    if file.startswith('.'):
                        new_name = file.lstrip('.')
                        new_path = os.path.join(root, new_name)
                        try:
                            os.rename(file_path, new_path)
                            fixed_count += 1
                        except Exception:
                            pass
                            
            self.result_lbl.text = f"تم الانتهاء بنجاح!\n- عدد الملفات المفحوصة: {scanned_count}\n- عدد الملفات التي تم إصلاحها وإظهارها: {fixed_count}"
            
        except Exception as e:
            self.result_lbl.text = f"حدث خطأ أثناء عملية الفحص والإصلاح:\n{str(e)}"

    def test_pillow(self, instance):
        try:
            version = PilImage.__version__
            self.result_lbl.text = f"مكتبة Pillow تعمل بكفاءة عالية!\nإصدار المكتبة: {version}"
        except Exception as e:
            self.result_lbl.text = f"خطأ في مكتبة Pillow: {str(e)}"

if __name__ == '__main__':
    KareemRepairApp().run()