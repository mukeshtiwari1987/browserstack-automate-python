# BrowserStack Client

This module interfaces all REST APIs offered by [BrowserStack](https://www.browserstack.com).

***This module is a work-in-progress.***

## Requirements

Please ensure that your BrowserStack account contains the required subscription(s) for using the APIs provided by this module.

Add your BrowserStack username and access key for Automate testing to the following environment variables for your shell.

```
BROWSERSTACK_USERNAME=<your-username>
BROWSERSTACK_KEY=<your-access-key>
```

## Usage
```
from BrowserStack_Library import BrowserStackLibrary

// BrowserStack Automate API
browserstack_obj = BrowserStackLibrary()
```
### Plan Information
Gets the information about your group's Automate plan, including the maximum number of parallel sessions allowed, the number of parallel sessions currently running and the number of parallel sessions queued
```
browserstack_obj.plans()
```
### All Available Browsers
Gets list of desired capabilities for both desktop and mobile browsers. It returns a flat hash in the format **[:os, :os_version, :browser, :browser_version, :device, :real_mobile]**
```
browserstack_obj.get_browsers()
```
### Plan Information
Fetches information about your group's Automate plan, including the maximum number of parallel sessions allowed, the number of parallel sessions currently running and the number of parallel sessions queued
```
browserstack_obj.plans()
```
### Build IDs
Get the build IDs
```
browserstack_obj.get_build_id()
```
### Session IDs
Get a JSON object with all the sessions
```
browserstack_obj.get_sessions()
```
### Active Session ID
Return the session ID of the first active session
```
browserstack_obj.get_active_session_id()
```
### Session Logs
Return the session log in text format
```
browserstack_obj.get_session_logs()
```
### Parallel Session Running
Get the number of parallel sessions currently running
```
browserstack_obj.parallel_sessions_running()
```
### Parallel Session Allowed
Get the number of parallel sessions allowed in group
```
browserstack_obj.parallel_sessions_max_allowed()
```
### Queued Session
Get the number of current queued sessions in group
```
browserstack_obj.queued_sessions()
```
### Queued Session Allowed
Get the number of queued sessions allowed in group
```
browserstack_obj.queued_sessions_max_allowed()
```
### Recycle Key
Destroys the current access key and returns a new access key.
```
browserstack_obj.recycle_key()
```