class EnterpriseOwnership:
    communal = 'Комунальна'
    private = 'Приватна'
    state = 'Державна'


ENTERPRISE_OWNERSHIP_CHOICES = (
    (EnterpriseOwnership.communal, "Комунальна"),
    (EnterpriseOwnership.private, "Приватна"),
    (EnterpriseOwnership.state, "Державна"),
)


class TaxType:
    atmosphere_tax = 'Atmosphere Tax'
    waterbody_tax = 'Waterbody Tax'
    placement_tax = 'Placement Tax'


TAX_TYPE_CHOICES = (
    (TaxType.atmosphere_tax, "Податок за забруднення атмосфери"),
    (TaxType.waterbody_tax, "Податок за забруднення водних об'єктів"),
    (TaxType.placement_tax, "Податок за розміщення відходів"),
)
