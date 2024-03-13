from quiz_struct import Quiz
import sample_01
import pcep_pe1_m1
import pcep_pe1_m2
import pcep_pe1_m3
import pcep_pe1_m4
import pcep_pe1_summary
import pcep_pe2_m1
import pcep_pe2_m2
import pcep_pe2_m3
import pcep_pe2_m4
import pcep_pe2_summary
import pcep_pe_final

AvailableExams = {
    sample_01.quiz_header: Quiz(sample_01.quiz_header, sample_01.quiz_description, sample_01.quiz_information, sample_01.quiz_link, sample_01.quiz),
    pcep_pe1_m1.quiz_header: Quiz(pcep_pe1_m1.quiz_header, pcep_pe1_m1.quiz_description, pcep_pe1_m1.quiz_information, pcep_pe1_m1.quiz_link, pcep_pe1_m1.quiz),
    pcep_pe1_m2.quiz_header: Quiz(pcep_pe1_m2.quiz_header, pcep_pe1_m2.quiz_description, pcep_pe1_m2.quiz_information, pcep_pe1_m2.quiz_link, pcep_pe1_m2.quiz),
    pcep_pe1_m3.quiz_header: Quiz(pcep_pe1_m3.quiz_header, pcep_pe1_m3.quiz_description, pcep_pe1_m3.quiz_information, pcep_pe1_m3.quiz_link, pcep_pe1_m3.quiz),
    pcep_pe1_m4.quiz_header: Quiz(pcep_pe1_m4.quiz_header, pcep_pe1_m4.quiz_description, pcep_pe1_m4.quiz_information, pcep_pe1_m4.quiz_link, pcep_pe1_m4.quiz),
    pcep_pe1_summary.quiz_header: Quiz(pcep_pe1_summary.quiz_header, pcep_pe1_summary.quiz_description, pcep_pe1_summary.quiz_information, pcep_pe1_summary.quiz_link, pcep_pe1_summary.quiz),
    pcep_pe2_m1.quiz_header: Quiz(pcep_pe2_m1.quiz_header, pcep_pe2_m1.quiz_description, pcep_pe2_m1.quiz_information, pcep_pe2_m1.quiz_link, pcep_pe2_m1.quiz),
    pcep_pe2_m2.quiz_header: Quiz(pcep_pe2_m2.quiz_header, pcep_pe2_m2.quiz_description, pcep_pe2_m2.quiz_information, pcep_pe2_m2.quiz_link, pcep_pe2_m2.quiz),
    pcep_pe2_m3.quiz_header: Quiz(pcep_pe2_m3.quiz_header, pcep_pe2_m3.quiz_description, pcep_pe2_m3.quiz_information, pcep_pe2_m3.quiz_link, pcep_pe2_m3.quiz),
    pcep_pe2_m4.quiz_header: Quiz(pcep_pe2_m4.quiz_header, pcep_pe2_m4.quiz_description, pcep_pe2_m4.quiz_information, pcep_pe2_m4.quiz_link, pcep_pe2_m4.quiz),
    pcep_pe2_summary.quiz_header: Quiz(pcep_pe2_summary.quiz_header, pcep_pe2_summary.quiz_description, pcep_pe2_summary.quiz_information, pcep_pe2_summary.quiz_link, pcep_pe2_summary.quiz),
    pcep_pe_final.quiz_header: Quiz(pcep_pe_final.quiz_header, pcep_pe_final.quiz_description, pcep_pe_final.quiz_information, pcep_pe_final.quiz_link, pcep_pe_final.quiz)
}