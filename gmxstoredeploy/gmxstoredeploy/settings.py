"""
Define confab environments and roles.
"""

environmentdefs = {
    'vagrant': ['gmxstore-vagrant']
}

componentdefs = {
    'web': ['python', 'nginx', 'supervisor', 'gmxstore'],
}

roledefs = {
    'web': ['gmxstore-vagrant'],
}
