
# Station marker types
STN_INTER = 0 # Standard interchange bullseye
STN_MINOR = 1 # Standard minor station (no interchanges, not stepfree)
STN_FSTEP = 2 # Fully stepfree (street to train)
STN_PSTEP = 3 # Partially stepfree (street to platform)

# Jubilee Line
jl_name = 'Jubilee Line'
jl_colour = (134,143,152)
jl_stations = (('Stanmore', STN_PSTEP),
                 ('Canons Park', STN_MINOR),
                 ('Queensbury', STN_MINOR),
                 ('Kingsbury', STN_PSTEP),
                 ('Wembley Park', STN_PSTEP),
                 ('Neasden', STN_MINOR),
                 ('Dollis Hill', STN_MINOR),
                 ('Willesden Green', STN_MINOR),
                 ('Kilburn', STN_PSTEP),
                 ('West Hampstead', STN_INTER),
                 ('Finchley Road', STN_INTER),
                 ('Swiss Cottage', STN_MINOR),
                 ('St John\'s Wood', STN_MINOR),
                 ('Baker Street', STN_INTER),
                 ('Bond Street', STN_INTER),
                 ('Green Park', STN_PSTEP),
                 ('Westminster', STN_FSTEP),
                 ('Waterloo', STN_FSTEP),
                 ('Southwark', STN_FSTEP),
                 ('London Bridge', STN_FSTEP),
                 ('Bermondsey', STN_FSTEP),
                 ('Canada Water', STN_FSTEP),
                 ('Canary Wharf', STN_FSTEP),
                 ('North Greenwich', STN_FSTEP),
                 ('Canning Town', STN_FSTEP),
                 ('West Ham', STN_FSTEP),
                 ('Stratford', STN_FSTEP))