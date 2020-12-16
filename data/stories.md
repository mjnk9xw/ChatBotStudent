## greet
* greet
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye

## thankyou
* thankyou
  - utter_noworries

## ask ability
* ask_ability
  - utter_show_ability

## getinfo
* getinfo
  - utter_getinfo

## setbot
* setbot
  - utter_setbot

## praise
* praise
  - utter_happy

## decry
* decry
  - utter_sorry

## school_rules
* school_rules
  - utter_school_rules

## school_score
* school_score
  - utter_school_score

## school_new
* school_new
  - utter_school_new

## school_web
* school_web
  - utter_school_web

## school_schedule
* school_schedule
  - utter_school_schedule

## school_student_info
* school_student_info
  - utter_school_student_info

## school_introduce
* school_introduce
  - utter_school_introduce

## school_intership
* school_intership
  - utter_school_intership

## tim_tailieu
* tim_tailieu
  - utter_tim_tailieu

## list_teacher
* list_teacher
  - utter_list_teacher

## dia_diem_phong_ban
* dia_diem_phong_ban
  - utter_dia_diem_phong_ban
## xin_giay_xac_nhan  
* xin_giay_xac_nhan
  - utter_xin_giay_xac_nhan
## dangky
* dangky
  - utter_dangky
## rut_hoc_phan
* rut_hoc_phan
  - utter_rut_hoc_phan
  ## khung_chuong_trinh
* khung_chuong_trinh
  - utter_khung_chuong_trinh
  ## hang_hoc_luc
* hang_hoc_luc
  - utter_hang_hoc_luc
<!-- ## search teacher infor : when everything goes well
* search_teacher_infor{"ten": "example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_teacher_infor{"mon_hoc": "example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_teacher_infor{"ma_mon_hoc": "example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

## search mon_hoc infor : when everything goes well
* search_mon_hoc_infor{"ten": "example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_mon_hoc_infor{"mon_hoc": "example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_mon_hoc_infor{"ma_mon_hoc": "example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

## search infor : when user didn't give an entity
* search_teacher_infor
  - utter_ask_teacher_name_or_course
  * inform{"ho_ten":"example"}
  - slot{"ho_ten":"example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_teacher_infor
  - utter_ask_teacher_name_or_course
  * inform{"mon_hoc":"example"}
  - slot{"mon_hoc":"example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_teacher_infor
  - utter_ask_teacher_name_or_course
  * inform{"ma_mon_hoc":"example"}
  - slot{"ma_mon_hoc":"example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug


## search infor : when user didn't give an entity
* search_mon_hoc_infor
  - utter_ask_mon_hoc
  * inform{"ho_ten":"example"}
  - slot{"ho_ten":"example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_mon_hoc_infor
  - utter_ask_mon_hoc
  * inform{"mon_hoc":"example"}
  - slot{"mon_hoc":"example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug

* search_mon_hoc_infor
  - utter_ask_mon_hoc
  * inform{"ma_mon_hoc":"example"}
  - slot{"ma_mon_hoc":"example"}
  - action_search_infor
  - slot{"ten":""}
  - slot{"mon_hoc":""}
  - slot{"ma_mon_hoc":""}
  - utter_debug -->

## story_01_tim_tai_lieu_toan_roi_rac

  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}
  * tim_tailieu
    - utter_subjects
  * tim_tailieu{"mon_hoc": "toán rời rạc"}
    - slot{"mon_hoc": "toán rời rạc"}
    - utter_tim_tailieu
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_01a_no_great_tim_tai_lieu_toan_roi_rac

  * tim_tailieu
    - utter_subjects
  * tim_tailieu{"mon_hoc": "toán rời rạc"}
    - slot{"mon_hoc": "toán rời rạc"}
    - utter_tim_tailieu
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye


 ## story_02_tim_tai_lieu_3D

  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}
  * tim_tailieu
    - utter_subjects
  * tim_tailieu{"mon_hoc": "Mô hình hóa 3d"}
    - slot{"mon_hoc": "Mô hình hóa 3d"}
    - utter_tim_tailieu
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

   ## story_02a_no_great_tim_tai_lieu_3D

  * tim_tailieu
    - utter_subjects
  * tim_tailieu{"mon_hoc": "Mô hình hóa 3d"}
    - slot{"mon_hoc": "Mô hình hóa 3d"}
    - utter_tim_tailieu
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

   ## story_03_tim_tai_lieu_he_dieu_hanh

  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_c hat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * tim_tailieu{"mon_hoc": "Lý Thuyết hệ điều hành"}
    - slot{"mon_hoc": "Lý Thuyết hệ điều hành"}
    - utter_tim_tailieu
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_03a_no_great_tim_tai_lieu_he_dieu_hanh

  * tim_tailieu{"mon_hoc": "Lý Thuyết hệ điều hành"}
    - slot{"mon_hoc": "Lý Thuyết hệ điều hành"}
    - utter_tim_tailieu
  * praise
    - utter_happy
  * goodbye 
    - utter_goodbye

  ## story_04_quy_che_daotao_phong_ban
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * quy_che_dao_tao
    - utter_quy_che_dao_tao
  * dia_diem_phong_ban
    - utter_dia_diem_phong_ban
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_05_quy_dinh_truong_lich_tiepssv 
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * quy_che_dao_tao
    - utter_quy_che_dao_tao  
  * dia_diem_phong_ban
    - utter_dia_diem_phong_ban
  * lich_tiep_sv
    - utter_lich_tiep_sv
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye


  ## story_04_quy_dinh_truong_giayxacnhan_1
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * xin_giay_xac_nhan
    - utter_xin_giay_xac_nhan
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_04a_quy_dinh_truong_giayxacnhan_1
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * xin_giay_xac_nhan
    - utter_xin_giay_xac_nhan
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_05_quy_dinh_truong_giayxacnhan_2
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * quy_che_dao_tao
    - utter_quy_che_dao_tao 
  * xin_giay_xac_nhan
    - utter_xin_giay_xac_nhan
  * lich_tiep_sv
    - utter_lich_tiep_sv
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_05_quy_dinh_truong_giayxacnhan_3
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * xin_giay_xac_nhan
    - utter_xin_giay_xac_nhan
  * dia_diem_phong_ban
    - utter_dia_diem_phong_ban
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_06_dangky_hocphan_1
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * dangky
    - utter_dangky
  * rut_hoc_phan
    - utter_rut_hoc_phan
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_07_dangky_hocphan_2
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * khung_chuong_trinh
    - utter_khung_chuong_trinh
  * dangky
    - utter_dangky
  * rut_hoc_phan
    - utter_rut_hoc_phan
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

  ## story_08_dangky_hocphan_2
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * khung_chuong_trinh
    - utter_khung_chuong_trinh
  * dangky
    - utter_dangky  
  * praise
    - utter_happy
  * goodbye
    - utter_goodbye

## story_09_muon_thi_lai
  * greet
    - utter_greet
  * getinfo{"name_user_chat": "Nguyễn Văn Minh"}
    - slot{"name_user_chat": "Nguyễn Văn Minh"}
    - utter_getinfo 
  * setbot{"name_chat": "Nguyễn Việt Anh"}
    - slot{"name_chat": "Nguyễn Việt Anh"}
    - utter_setbot{}

  * hang_hoc_luc
    - utter_hang_hoc_luc
  * thi_lai
    - utter_thi_lai  

  ## story_10_muon_thi_lai
    
  * thi_lai
    - utter_thi_lai

  
  










