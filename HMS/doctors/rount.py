
def show_doctors(content_frame):
    from HMS.doctors.doctorsPage import doctors_items
    doctors_items(content_frame)

def show_doctor_details(content_frame, doctor_id):
    from HMS.doctors.doctorDetails import open_doctor_details
    open_doctor_details(content_frame, doctor_id)