from datetime import date


class DomainAssessment:
    """
    Assessment domain model.
    """

    def __init__(self, id, date, score, percent_complete, comments, status, site_location, assessment_template_id, alignment_engineer_id, customer_id):
        self.id = id
        self.date = date
        self.score = score
        self.percent_complete = percent_complete
        self.comments = comments
        self.status = status
        self.site_location = site_location
        self.assessment_template_id = assessment_template_id
        self.alignment_engineer_id = alignment_engineer_id
        self.customer_id = customer_id

    def __str__(self):
        return f"Assessment ID: {self.id}, Date: {self.date}, Score: {self.score}"
