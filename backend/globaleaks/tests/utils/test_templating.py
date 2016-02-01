# -*- encoding: utf-8 -*-

from twisted.internet.defer import inlineCallbacks

from globaleaks.handlers import admin, rtip
from globaleaks.jobs.delivery_sched import DeliverySchedule
from globaleaks.tests import helpers
from globaleaks.utils.templating import Templating, supported_template_types, \
    TipKeyword, CommentKeyword, MessageKeyword, FileKeyword


class notifTemplateTest(helpers.TestGLWithPopulatedDB):
    @inlineCallbacks
    def test_keywords_conversion(self):
        yield self.perform_full_submission_actions()
        yield DeliverySchedule().operation()

        data = {}
        data['type'] = 'tip'
        data['receiver'] = yield admin.receiver.get_receiver(self.dummyReceiver_1['id'], 'en')
        data['context'] = yield admin.context.get_context(self.dummyContext['id'], 'en')
        data['notification'] = yield admin.notification.get_notification('en')
        data['node'] = yield admin.node.admin_serialize_node('en')
        data['tip'] = self.dummyRTips[0]
        comments = yield rtip.get_comment_list(self.dummyReceiver_1['id'], data['tip']['id'])
        data['comment'] = comments[0]
        messages = yield rtip.get_message_list(self.dummyReceiver_1['id'], data['tip']['id'])
        data['message'] = messages[0]
        files = yield rtip.get_files_receiver(self.dummyReceiver_1['id'], data['tip']['id'])
        data['file'] = files[0]

        for key in ['tip', 'comment', 'message', 'file']:
            data['type'] = key
            template = ''.join(supported_template_types[key].keyword_list)
            ret = Templating().format_template(template, data)
