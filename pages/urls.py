from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^goods/(?P<off_url>[A-Za-z0-9_-]+)/$', OfferAjaxUpdateView.as_view(), name='offer'),
    url(r'^goods/(?P<off_url>[A-Za-z0-9_-]+)/images/$', OfferImagesAjaxUpdateView.as_view(), name='offer_images'),
    url(r'^images_form/(?P<obj_id>[0-9]+)$', OfferImagesAjaxUpdateView.as_view(), name='offer_images_by_id'),
    #   url(r'^fb_post$', fb_post, name='fb_post'),
    #   url(r'^lb_post$', lb_post, name='lb_post'),

    url(r'^edit-ajax-forms/.*\.html$', AdminAjaxEditForm.as_view(), name='admin-edit-form'),

    # url(r'^ac_post$', ac_post, name='ac_post'),
    # url(r'^to_post$', to_post, name='to_post'),
    # url(r'^sup_post$', sup_post, name='sup_post'),
    # url(r'^p_post$', p_post, name='p_post'),
    # url(r'^company_post$', company_post, name='company_post'),

    url(r'^comment_admin$', comment_admin, name='comment_admin'),
    url(r'^delete$', comment_delete, name='comment_delete'),
    # url(r'^1g$', pars_cat),
    # url(r'^2g$', pars_goods),
    url(r'^catalog/(?P<cat_url>[A-Za-z0-9_-]+)$', catalog, name='catalog'),
    url(r'^otzyvy', review, name='review'),
    url(r'^catalog', catalog, name='cat_redirect'),
    url(r'^api-import$', api_import, name='api_import'),
    url(r'^(?P<post_seourl>[A-Za-z0-9_-]+)$', SinglePageAjaxUpdateView.as_view(), name='post'),
    url(r'^$', Home.as_view(), name='home'),
]
