import requests
import json


class BrowserStackLibrary:
    """"BrowserStack library to interact with BrowserStack artifacts"""

    def __init__(self, credentials_file=None):
        """Constructor for the BrowserStack library"""
        self.browserstack_url = "https://api.browserstack.com/automate/"
        self.auth = ('carlisle2', 'JxXoDtSiTpmyXk72u4yQ')

    def plans(self):
        "Get information about your Group's Automate plan"
        self.plan_url = self.browserstack_url + "plan.json"
        plans = requests.get(self.plan_url, auth=self.auth).json()

        return plans

    def get_browsers(self):
        """Returns list of Desktop and Mobile browsers offered for Automate."""
        self.browsers_url = self.browserstack_url + "browsers.json"
        browsers = requests.get(self.browsers_url, auth=self.auth).json()

        return browsers

    def get_build_id(self):
        """"Get the build ID"""
        self.build_url = self.browserstack_url + "builds.json"
        builds = requests.get(self.build_url, auth=self.auth).json()
        build_id = builds[0]['automation_build']['hashed_id']

        return build_id

    def get_sessions(self):
        """"Get a JSON object with all the sessions"""
        build_id = self.get_build_id()
        sessions = requests.get(self.browserstack_url + 'builds/%s/sessions.json' % build_id, auth=self.auth).json()

        return sessions

    def get_active_session_id(self):
        """Return the session ID of the first active session"""
        session_id = None
        sessions = self.get_sessions()
        for session in sessions:
            # Get session id of the first session with status = running
            if session['automation_session']['status'] == 'running':
                session_id = session['automation_session']['hashed_id']
                break

        return session_id

    def get_session_url(self, session_id):
        """Get the video URL from build and session details. Needs to be called after session is completed"""
        build_id = self.get_build_id()
        self.build_session_url = self.browserstack_url + "builds/" + build_id + "/sessions/" + session_id
        build_session_details = requests.get(self.build_session_url, auth=self.auth).json()

        # Get the video url from session details
        video_url = build_session_details[u'automation_session'][u'video_url']
        session_url = video_url.encode("utf-8")

        return session_url

    def get_session_logs(self):
        """Return the session log in text format"""
        build_id = self.get_build_id()
        session_id = self.get_active_session_id()
        session_log = requests.get(self.browserstack_url + 'builds/%s/sessions/%s/logs' % (build_id, session_id),
                                   auth=self.auth).text

        return session_log

    def parallel_sessions_running(self):
        """Get the number of parallel sessions currently running"""
        plans = self.plans()
        parallel_sessions_running = plans["parallel_sessions_running"]

        return parallel_sessions_running

    def parallel_sessions_max_allowed(self):
        """Get the number of parallel sessions allowed in group"""
        plans = self.plans()
        parallel_sessions_max_allowed = plans["parallel_sessions_max_allowed"]

        return parallel_sessions_max_allowed

    def queued_sessions(self):
        """Get the number of current queued sessions in group"""
        plans = self.plans()
        queued_sessions = plans["queued_sessions"]

        return queued_sessions

    def queued_sessions_max_allowed(self):
        """Get the number of queued sessions allowed in group"""
        plans = self.plans()
        queued_sessions_max_allowed = plans["queued_sessions_max_allowed"]

        return queued_sessions_max_allowed

    def get_latest_screenshot_url(self):
        """Get the URL of the latest screenshot"""
        session_log = self.get_session_logs()

        # Process the text to locate the URL of the last screenshot

        screenshot_request = session_log.split('screenshot {}')[-1]
        response_result = screenshot_request.split('REQUEST')[0]
        image_url = response_result.split('https://')[-1]
        image_url = image_url.split('.png')[0]
        screenshot_url = 'https://' + image_url + '.png'

        return screenshot_url

    def recycle_key(self):
        """Destroys the current access key and returns a new access key."""
        self.recycle_url = self.browserstack_url + "recycle_key.json"
        new_key = requests.put(self.recycle_url, auth=self.auth).json()['new_key']

        return new_key
