from django.test import TestCase

# Create your tests here.
# def late_fine(student_pk):
#     """
#     This View Is connected with daj
#     """
#     student = get_object_or_404(MyUser, pk=student_pk)
#     student_info = Student_Information.objects.get(user=student)  # Retrieve Student_Information instance
#     borrowings = Borrower.objects.filter(book_borrower_student=student_info) 
#     # print(student, student_info, borrowings)
#     total_fine = 0
#     for borrowing in borrowings:
#         # if borrowing.return_date is None:  # Check if book has not been returned yet
#         #     borrowing.return_date = dt.today()  # Set the return_date to the current datetime
#         #     borrowing.save()  # Save the changes
#         fine = borrowing.overdue_fine()  # Pass the student instance
#         total_fine += fine
#         if total_fine > 0:
#             student_info.Penalty = str(total_fine)
#             student_info.save()
#         else:
#             pass
#         response_data = {"total_fine": total_fine}
#         return JsonResponse(response_data)

def late_fine(student_pk):
    """
    Calculate the total fine for the student.
    """
    student = get_object_or_404(MyUser, pk=student_pk)
    student_info = get_object_or_404(Student_Information, user=student)
    borrowings = Borrower.objects.filter(book_borrower_student=student_info)
    total_fine = sum(borrowing.overdue_fine() for borrowing in borrowings)
    # Save total fine to student_info
    if total_fine > 0:
        student_info.Penalty = str(total_fine)
        student_info.save()
    return total_fine