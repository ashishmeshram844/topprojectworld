from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('admin_base',views.admin_base,name='admin_base'),

   path('admin-login',views.admin_login,name='admin-login'),
   path('admin-logout',views.admin_logout,name='admin-logout'),

   path('admin_home',views.admin_home,name='admin_home'),
   path('user_enquiry_list',views.user_enquiry_list,name='user_enquiry_list'),



   #STUDENT
   path('add_new_user',views.add_new_user,name='add_new_user'),
   path('users_list',views.users_list,name='users_list'),
   path('delete_user/<int:myid>/',views.delete_user,name='delete_user'),
   path('block_user/<int:myid>/',views.block_user,name='block_user'),
   path('unblock_user/<int:myid>/',views.unblock_user,name='unblock_user'),
   path('view_user/<int:myid>/',views.view_user,name='view_user'),
   path('user_bookmark_list',views.user_bookmark_list,name='user_bookmark_list'),


   #PROJECT
   path('add_project_catagory',views.add_project_catagory,name='add_project_catagory'),
   path('project_catagory_list',views.project_catagory_list,name='project_catagory_list'),
   path('delete_project_catagory/<int:myid>/',views.delete_project_catagory,name='delete_project_catagory'),
   path('view_project_catagory/<int:myid>/',views.view_project_catagory,name='view_project_catagory'),
   path('update_project_catagory/<int:myid>/',views.update_project_catagory,name='update_project_catagory'),

   path('add_technology',views.add_technology,name='add_technology'),
   path('technology_list',views.technology_list,name='technology_list'),
   path('delete_technology/<int:myid>/',views.delete_technology,name='delete_technology'),
   path('view_technology/<int:myid>/',views.view_technology,name='view_technology'),
   path('update_technology/<int:myid>/',views.update_technology,name='update_technology'),

   path('add_os',views.add_os,name='add_os'),
   path('os_list',views.os_list,name='os_list'),
   path('delete_os/<int:myid>/',views.delete_os,name='delete_os'),
   path('view_os/<int:myid>/',views.view_os,name='view_os'),
   path('update_os/<int:myid>/',views.update_os,name='update_os'),


   path('add_project',views.add_project,name='add_project'),
   path('project_list',views.project_list,name='project_list'),
   path('delete_project/<int:myid>/',views.delete_project,name='delete_project'),
   path('view_project/<int:myid>/',views.view_project,name='view_project'),
   path('update_project/<int:myid>/',views.update_project,name='update_project'),



   path('add_project_technology',views.add_project_technology,name='add_project_technology'),
   path('project_technology_list',views.project_technology_list,name='project_technology_list'),
   path('delete_pro_tech/<int:myid>/',views.delete_pro_tech,name='delete_pro_tech'),
   path('view_pro_tech/<int:myid>/',views.view_pro_tech,name='view_pro_tech'),
   path('update_pro_tech/<int:myid>/',views.update_pro_tech,name='update_pro_tech'),


   path('add_project_screenshot',views.add_project_screenshot,name='add_project_screenshot'),
   path('project_screenshot_list',views.project_screenshot_list,name='project_screenshot_list'),
   path('delete_pro_screen/<int:myid>/',views.delete_pro_screen,name='delete_pro_screen'),
   path('view_pro_screen/<int:myid>/',views.view_pro_screen,name='view_pro_screen'),
   path('update_pro_screen/<int:myid>/',views.update_pro_screen,name='update_pro_screen'),



   path('add_project_file',views.add_project_file,name='add_project_file'),
   path('project_file_list',views.project_file_list,name='project_file_list'),
   path('delete_project_file/<int:myid>/',views.delete_project_file,name='delete_project_file'),
   path('view_project_file/<int:myid>/',views.view_project_file,name='view_project_file'),
   path('update_project_file/<int:myid>/',views.update_project_file,name='update_project_file'),



   path('add_project_os',views.add_project_os,name='add_project_os'),
   path('project_os_list',views.project_os_list,name='project_os_list'),
   path('delete_project_os/<int:myid>/',views.delete_project_os,name='delete_project_os'),

   path('add_project_module',views.add_project_module,name='add_project_module'),
   path('project_module_list',views.project_module_list,name='project_module_list'),
   path('delete_project_module/<int:myid>/',views.delete_project_module,name='delete_project_module'),
   path('view_project_module/<int:myid>/',views.view_project_module,name='view_project_module'),
   path('update_project_module/<int:myid>/',views.update_project_module,name='update_project_module'),


   path('project_review_list',views.project_review_list,name='project_review_list'),
   path('delete_project_review/<int:myid>/',views.delete_project_review,name='delete_project_review'),

    path('project_enquiry_list',views.project_enquiry_list,name='project_enquiry_list'),


   path('add_subject_catagory',views.add_subject_catagory,name='add_subject_catagory'),
   path('subject_catagory_list',views.subject_catagory_list,name='subject_catagory_list'),
   path('delete_sub_cat/<int:myid>/',views.delete_sub_cat,name='delete_sub_cat'),
   path('view_sub_cat/<int:myid>/',views.view_sub_cat,name='view_sub_cat'),
   path('update_sub_cat/<int:myid>/',views.update_sub_cat,name='update_sub_cat'),




   path('add_subject',views.add_subject,name='add_subject'),
   path('subject_list',views.subject_list,name='subject_list'),
   path('delete_subject/<int:myid>/',views.delete_subject,name='delete_subject'),
   path('view_subject/<int:myid>/',views.view_subject,name='view_subject'),
   path('update_subject/<int:myid>/',views.update_subject,name='update_subject'),


   path('add_program',views.add_program,name='add_program'),
   path('program_list',views.program_list,name='program_list'),
   path('delete_program/<int:myid>/',views.delete_program,name='delete_program'),
   path('view_program/<int:myid>/',views.view_program,name='view_program'),
   path('update_program/<int:myid>/',views.update_program,name='update_program'),


   path('add_chapter',views.add_chapter,name='add_chapter'),
   path('chapter_list',views.chapter_list,name='chapter_list'),
   path('delete_chapter/<int:myid>/',views.delete_chapter,name='delete_chapter'),
   path('view_chapter/<int:myid>/',views.view_chapter,name='view_chapter'),
   path('update_chapter/<int:myid>/',views.update_chapter,name='update_chapter'),



   path('add_topic',views.add_topic,name='add_topic'),
   path('topic_list',views.topic_list,name='topic_list'),
   path('delete_topic/<int:myid>/',views.delete_topic,name='delete_topic'),
   path('view_topic/<int:myid>/',views.view_topic,name='view_topic'),
   path('update_topic/<int:myid>/',views.update_topic,name='update_topic'),


   path('add_tutorial_detail',views.add_tutorial_detail,name='add_tutorial_detail'),
   path('tutorial_detail_list',views.tutorial_detail_list,name='tutorial_detail_list'),
   path('delete_tutorial_detail/<int:myid>/',views.delete_tutorial_detail,name='delete_tutorial_detail'),
   path('view_tutorial_detail/<int:myid>/',views.view_tutorial_detail,name='view_tutorial_detail'),
   path('update_tutorial_detail/<int:myid>/',views.update_tutorial_detail,name='update_tutorial_detail'),





   path('homepage_slider_list',views.homepage_slider_list,name='homepage_slider_list'),
   path('view_homepage_slider/<int:myid>/',views.view_homepage_slider,name='view_homepage_slider'),
   path('update_home_slider/<int:myid>/',views.update_home_slider,name='update_home_slider'),


   path('add_homepage_discover_more',views.add_homepage_discover_more,name='add_homepage_discover_more'),
   path('discover_more_list',views.discover_more_list,name='discover_more_list'),
   path('delete_discover_more_link/<int:myid>/',views.delete_discover_more_link,name='delete_discover_more_link'),
   path('view_discover_more/<int:myid>/',views.view_discover_more,name='view_discover_more'),
   path('update_discover_more_link/<int:myid>/',views.update_discover_more_link,name='update_discover_more_link'),



   path('about_us_page',views.about_us_page,name='about_us_page'),
   path('about_us_page_list',views.about_us_page_list,name='about_us_page_list'),
   path('view_about_us/<int:myid>/',views.view_about_us,name='view_about_us'),
   path('update_about_us_page/<int:myid>/',views.update_about_us_page,name='update_about_us_page'),
   path('delete_about_item/<int:myid>/',views.delete_about_item,name='delete_about_item'),




   path('contact_us_page',views.contact_us_page,name='contact_us_page'),
   path('update_contact_us_page/<int:myid>/',views.update_contact_us_page,name='update_contact_us_page'),



   path('add_blog',views.add_blog,name='add_blog'),

   path('blog_list',views.blog_list,name='blog_list'),

   path('view_blog/<int:myid>/',views.view_blog,name='view_blog'),

   path('update_blog_detail/<int:myid>/',views.update_blog_detail,name='update_blog_detail'),

   path('delete_blog/<int:myid>/',views.delete_blog,name='delete_blog'),


   path('add_seo_script',views.add_seo_script,name='add_seo_script'),

   path('keyward_list',views.keyward_list,name='keyward_list'),


   path('sold_project_list',views.sold_project_list,name='sold_project_list'),




]