from django import forms

BEDROOM_CHOICES = (
    ("ALL", "Bedrooms (Any)"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10")
)

MAX_PRICE_CHOICES = (
    ("ALL", "Max Price (All)"),
    (100000, "$100,000"),
    (200000, "$200,000"),
    (300000, "$300,000"),
    (400000, "$400,000"),
    (500000, "$500,000"),
    (600000, "$600,000"),
    (700000, "$700,000"),
    (800000, "$800,000"),
    (900000, "$900,000"),
    (1000000, "$1M+"),
)

STATE_CHOICES = (
    ("ALL", "All States"),
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("DC", "District Of Columbia"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming")
)


class SearchForm(forms.Form):
    bedrooms = forms.ChoiceField(choices=BEDROOM_CHOICES, required=False)
    bedrooms.widget.attrs.update({'class': 'form-control'})

    city = forms.CharField(required=False)
    city.widget.attrs.update({'class': 'form-control', 'placeholder': 'City'})

    keywords = forms.CharField(required=False)
    keywords.widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword (Pool, Garage, etc)'})

    max_price = forms.ChoiceField(choices=MAX_PRICE_CHOICES, required=False)
    max_price.widget.attrs.update({'class': 'form-control'})

    state = forms.ChoiceField(choices=STATE_CHOICES, required=False)
    state.widget.attrs.update({'class': 'form-control'})
