# Database tables info


table_info = {
    'Album': ['AlbumId', 'Title', 'ArtistId'],
    'Artist': ['ArtistId', 'Name'],
    'Customer': ['CustomerId', 'FirstName', 'LastName', 'Company', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email', 'SupportRepId'],
    'Employee': ['EmployeeId', 'LastName', 'FirstName', 'Title', 'ReportsTo', 'BirthDate', 'HireDate', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email'],
    'Genre': ['GenreId', 'Name'],
    'Invoice': ['InvoiceId', 'CustomerId', 'InvoiceDate', 'Total'],
    'InvoiceLine': ['InvoiceLineId', 'InvoiceId', 'TrackId', 'UnitPrice', 'Quantity'],
    'MediaType': ['MediaTypeId', 'Name'],
    'Playlist': ['PlaylistId', 'Name'],
    'PlaylistTrack': ['PlaylistId', 'TrackId'],
    'Track': ['TrackId', 'Name', 'AlbumId', 'MediaTypeId', 'GenreId', 'Composer', 'Milliseconds', 'Bytes', 'UnitPrice']}

