"""
Courses API URI specification
The order of the URIs really matters here, due to the slash characters present in the identifiers
"""
from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from api_manager import courses_views

urlpatterns = patterns('',
    url(r'/*$^', courses_views.CoursesList.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)$', courses_views.CoursesDetail.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/modules/(?P<module_id>[a-zA-Z0-9/_:]+)/submodules/*$', courses_views.ModulesList.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/modules/(?P<module_id>[a-zA-Z0-9/_:]+)$', courses_views.ModulesDetail.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/modules/*$', courses_views.ModulesList.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/groups/(?P<group_id>[0-9]+)$', courses_views.CoursesGroupsDetail.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/groups/*$', courses_views.CoursesGroupsList.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/overview$', courses_views.CoursesOverview.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/updates$', courses_views.CoursesUpdates.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/static_tabs/(?P<tab_id>[a-zA-Z0-9/_:]+)$', courses_views.CoursesStaticTabsDetail.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/static_tabs$', courses_views.CoursesStaticTabsList.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/users/(?P<user_id>[0-9]+)$', courses_views.CoursesUsersDetail.as_view()),
    url(r'^(?P<course_id>[^/]+/[^/]+/[^/]+)/users$', courses_views.CoursesUsersList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)