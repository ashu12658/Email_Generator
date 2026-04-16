test_cases = [

    {
        "intent": "Clarify interview feedback confusion",
        "facts": [
            "Recruiter said feedback will come this week",
            "No update received yet",
            "Interview panel mentioned different timeline"
        ],
        "tone": "professional",
        "reference_email": """Subject: Follow-up on Interview Feedback

Dear Hiring Team,

I hope you are doing well. I wanted to clarify the feedback timeline as I was informed that the recruiter would share updates this week, but I have not yet received any response.

During the interview, a different timeline was also mentioned by the panel, so I wanted to confirm the current status.

Looking forward to your update.

Sincerely,
[Your Name]"""
    },

    {
        "intent": "Follow up on discussion",
        "facts": [
            "Discussion happened recently",
            "Waiting for response"
        ],
        "tone": "formal",
        "reference_email": """Subject: Follow-up on Recent Discussion

Dear Sir/Madam,

I am writing to follow up on our recent discussion. I am currently awaiting your response regarding the same.

Kindly let me know if any further details are required from my side.

Regards,
[Your Name]"""
    },

    {
        "intent": "Apologize and request reschedule for missed client meeting",
        "facts": [
            "Missed meeting due to power outage",
            "Client was waiting at 4 PM",
            "Need to reschedule next week"
        ],
        "tone": "apologetic",
        "reference_email": """Subject: Apology for Missed Meeting

Dear Client,

I sincerely apologize for missing our scheduled meeting at 4 PM due to an unexpected power outage.

I understand the inconvenience caused and would like to request a reschedule for next week at your convenience.

Thank you for your understanding.

Sincerely,
[Your Name]"""
    },

    {
        "intent": "Urgent complaint about broken service",
        "facts": [
            "Service stopped working suddenly",
            "Business operations impacted",
            "Support ticket raised but no response"
        ],
        "tone": "firm",
        "reference_email": """Subject: Urgent Complaint Regarding Service Outage

Dear Support Team,

I am writing to urgently report that the service has stopped working suddenly, causing significant disruption to our business operations.

Despite raising a support ticket, I have not received any response. This issue requires immediate attention.

Regards,
[Your Name]"""
    },

    {
        "intent": "Project status update email",
        "facts": [
            "Backend completed",
            "Frontend 80% done",
            "Testing started",
            "Deployment planned next week",
            "Minor bugs identified",
            "Client review pending"
        ],
        "tone": "professional",
        "reference_email": """Subject: Project Status Update

Dear Team,

Here is the current project update:

Backend has been completed and frontend development is 80% done. Testing has started, and deployment is planned for next week.

A few minor bugs have been identified, and client review is still pending.

Regards,
[Your Name]"""
    },

    {
        "intent": "Request leave due to personal emergency",
        "facts": [
            "Family emergency occurred",
            "Need 3 days leave",
            "Work handover completed"
        ],
        "tone": "empathetic",
        "reference_email": """Subject: Leave Request

Dear Manager,

I am writing to inform you about a personal family emergency that requires my immediate attention.

I would like to request 3 days of leave. I have already completed the necessary work handover to ensure smooth operations.

Thank you for your understanding.

Sincerely,
[Your Name]"""
    },

    {
        "intent": "General follow-up email",
        "facts": [
            "Waiting for update"
        ],
        "tone": "polite",
        "reference_email": """Subject: Follow-up

Dear Sir/Madam,

I hope you are doing well. I am writing to kindly follow up as I am still waiting for an update.

Looking forward to your response.

Regards,
[Your Name]"""
    },

    {
        "intent": "Escalate unresolved issue to manager",
        "facts": [
            "Issue open for 10 days",
            "Support team unresponsive",
            "Business impact increasing"
        ],
        "tone": "formal",
        "reference_email": """Subject: Escalation of Unresolved Issue

Dear Manager,

I am writing to escalate an issue that has been open for the past 10 days with no resolution.

The support team has not been responsive, and the issue is now impacting business operations.

Kindly look into this matter urgently.

Regards,
[Your Name]"""
    },

    {
        "intent": "Thank and politely reject offer",
        "facts": [
            "Received job offer",
            "Decided to pursue other opportunity",
            "Appreciate consideration"
        ],
        "tone": "polite but firm",
        "reference_email": """Subject: Job Offer Decision

Dear Hiring Team,

Thank you very much for offering me the position. I truly appreciate the opportunity and your consideration.

After careful evaluation, I have decided to pursue another opportunity that aligns with my current goals.

Thank you once again.

Sincerely,
[Your Name]"""
    },

    {
        "intent": "Schedule urgent meeting with team",
        "facts": [
            "Project deadline approaching",
            "Team availability needed ASAP",
            "Meeting requested within 48 hours"
        ],
        "tone": "professional urgent",
        "reference_email": """Subject: Urgent Meeting Request

Dear Team,

As the project deadline is approaching, I would like to schedule an urgent meeting to align on remaining tasks.

Please confirm your availability within the next 48 hours so we can proceed accordingly.

Regards,
[Your Name]"""
    }
]