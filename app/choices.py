class EnterpriseOwnership:
    communal = 'Комунальна'
    private = 'Приватна'
    state = 'Державна'


ENTERPRISE_OWNERSHIP_CHOICES = (
    (EnterpriseOwnership.communal, "Комунальна"),
    (EnterpriseOwnership.private, "Приватна"),
    (EnterpriseOwnership.state, "Державна"),
)
