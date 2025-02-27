from django import forms

ISSUE_TYPES =( 
    ("pothole","Pothole"),
    ("street_lighting","Street lighting"),
    ("graffiti","Graffiti"),
    ("asob","Anti-Social behaviour"),
    ("fly_tipping","Fly-Tipping"),
    ("drains", "Blocked Drains")
) 

class LogIssue(forms.Form):
    issue_type = forms.ChoiceField(
        choices=ISSUE_TYPES,
        label="Issue: "
        )
    issue_desc = forms.CharField(
        required=False,
        widget=forms.Textarea()
        )