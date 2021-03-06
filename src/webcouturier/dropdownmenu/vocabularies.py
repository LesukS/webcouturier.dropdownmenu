# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from Products.CMFCore.utils import getToolByName

from webcouturier.dropdownmenu import msg_fact as _

from zope.component.hooks import getSite


def format_size(size):
    return size.split(' ')[0]


def SizeVocabulary(context):
        image_terms = [
            SimpleTerm('none', 'none', _(u"label_size_none",
                                         default=u'None'))
        ]
        site = getSite()
        portal_properties = getToolByName(site, 'portal_properties', None)
        # here we add the custom image sizes, we skip the two largest
        if 'imaging_properties' in portal_properties.objectIds():
            sizes = portal_properties.imaging_properties.getProperty(
                'allowed_sizes')
            terms = [SimpleTerm(value=format_size(pair),
                                token=format_size(pair),
                                title=pair) for pair in sizes
                     if not format_size(pair) in ['preview', 'large']]
            image_terms = image_terms + terms

        return SimpleVocabulary(image_terms)
