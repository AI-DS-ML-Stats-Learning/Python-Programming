1. pd.read_csv -> to read csv files
2. pd.set_options('display.max_columns', col_length) -> displays all columns in the df
3. pd.set_option('display.max_rows', 85) -> displays the top 85 rows fully
4. pandas.Series -> means rows of data with a single col
5. type(df['col_name']) -> gives the type of the column
6. columns in a df can be accessed both by df['col_name'] and df.email (dot notation) -> they both return the same thing. But the bracket one is preferred to avoid conflicting with any of the methods of a dataframe [sometimes we keep a column name matching with a dataframe method, and that can cause problem with dot notation]
7. how top access rows and columns - 
    a. loc -> df.loc[[0,1], ['email', 'first']] (loc works with indices and col names)
    b. iloc -> df.iloc[[0,1], [2, 1]] (iloc works positions)
8. value_counts() -> count values in a dataframe in a column [basically group by a column ande get the count of the values inside it]
9. isin() - This is a method to filter for specific values in a df. filt = df['Country'].isin(countries) -> here countries is a list of values and we are filtering the df for only those countries
10. str.contains() - This is a dynamic string checker, that whether a string exists inside a column. filt = df['LanguageWorkedWith'].str.contains('Python', na = False) -> here we are checking if 'Python' exists within the particular col of df. And na=False means, if we find any na values, we will label it as False, since the en tire operation anyway returns a boolean result
11. & - This is 'and' operator used for filtering data
12. | - This is 'or' operator used for filtering data
13. ~ - This is 'negate' operator used for filtering data, as in, whataver is applicable as per the filter remove those.
14. df.rename(columns = {old:new}) -> columns can be renamed using this
15. using list comprehensions also column names can be updated
16. df.columns = df.columns.str.replace(' ', '_') -> replace a character in the column names
17. Modify data rows in a Dataframe using the following - 
    a. apply -> dataframe/ series object 
        df['email'] = df['email'].apply(lambda x : x.lower()) -> lambda functions  or any UDF can also be used here.
    b. map -> this works on both series and a dataframe object. This also replaced applymap. 
        df.map(str.lower) -> lowercase all the values in the dataframe
        df['first'].map({'Salil':'Chris', 'Jane':'Mary'}) -> #map usually substitute values but only for those that are mentioned. For those that aren't mentioned are substituted with NaN
    c. applymap -> this is deprecated
    d. replace -> it replaces the values only those are required, and leaves the rest as is, does not modifies them to NaN or something
18. df.at[2, 'col_name'] and df.iat[2, 1] -> works only with single cell operation, cannot take list parameters like loc/iloc
19. Drop columns in dataframe = df.drop(columns = ['col_name], inplace = True)
20. Split & expand 1 col into multiple = 
    df['full_name'].str.split(' ')
    df[['first','last']] = df['full_name'].str.split(' ', expand=True)
21. Set index - 
    a. While loading the df -> df = pd.read_csv('path/file_name', index_col = 'col_name')
    b. after loading the df -> df.set_index('col_name', inplace = True) 
22. Sorting a df by - 
    a. index - df.sort_index(ascending = False, inplace = True)
    b. values - df.sort_values(by = ['last', 'first'], ascending=[False, True], inplace=True)
23. Reset index using -> df.reset_index(inplace = True) 
    This operation will remove all index rules we applied explicitly on df for any col or so. Means, index will be back to 0,1,2,3 naming
24. To apply multiple filters, each conditions shouold be enclosed withing braces -> filt = (condition 1) | (condition 2)
25. df.columns = [x.upper() for x in df.columns] -> if operating on col names
26. df.loc[0:2, 'Hobbyist':'Employment'] -> this filters columns from a to b where both are inclusive
27. Functions (Apply) vs Map -> applying conditional logics
    """
    def update_hobbyist(Hobbyist):
        if Hobbyist == 'Yes':
            return True
        else:
            return False

    df['Hobbyist'].apply(update_hobbyist)

    df['Hobbyist'] = df['Hobbyist'].map({'Yes':True, 'No':False})
    df['Hobbyist']
    """
28. Get highest and smallest values - 
    a. nlargest -> df['ConvertedComp'].nlargest(10)
        Gives top 10 values of the col
    b. nsmallest -> df['ConvertedComp'].nsmallest(10)
        Gives top 10 values of the col
    c. df.nlargest(10, 'ConvertedComp') -> Returns the dataframe with the top 10 values of the col
29. Apply aggregations on all numerical cols of the df -> df.median(numeric_only=True)
30. df.describe() -> provides a summary od the data, all metricws = mean, median, percentile, etc
31. GroupBy in Pandas -> 
    Spliting the Object + Applying the function + Combine the Results
32. df['SocialMedia'].value_counts(normalize = True) -> normalize shoes percent distribution of the value_count data
33. Work with GroupBys - 
    a. create groups -> country_group = df.groupby('Country')
    b. country_group.groups.keys() -> this holds all the possible groups
    c. Fetch Groups -> country_group.get_group('India') = this gives a subset of the original df but only for Country India
    d. country_group['SocialMedia'].value_counts() -> fetch count of rows ona specific col inside the groups. This returns a grouped data at Country and SocialMedia level, with count of rows
    e. country_group['SocialMedia'].value_counts().loc['India'] -> can still filter on the df created, but only on the grouped column, as post aggregation, we lost the original df.
34. Fetch Multiple aggregations using Agg Method - 
    a. country_group['ConvertedComp'].agg(['median', 'mean'])
35. Dealing with null/nan values - 
    a. df.dropna -> drops all the rows with null values
        df.dropna(axis = 'index', how = 'any') #default method -> this means any value in a row is null,drop it
    b. If we want to drop only those rows where all of its cell values are null, then we change the 'how' to 'all'
        df.dropna(axis = 'index', how = 'all')
    c. axis - 
        1. if index -> Means drop rows
        2. if columns -> Means drop columns
    d. We can also subset on columns -> df.dropna(axis = 'index', how = 'any', subset = ['email']) 
        This means drop all the rows where column 'email' has null values
    e. We can also replace null values using replace method -> df.replace('NA', np.na, inplace = True)
        This basically all custom missingg values that do not get caught by dropna, we convert them to python detectable 'na' values so that when we apply dropna, these are detected and removed
    f. .isna() -> This returns a dataframe of boolean values
    g. fillna() -> We can also replace nulls with specific values if we do not want to drop the rows directly
        df.fillna('MISSING')
36. Casting data types -> astype()
37. unique() -> this gives unique /distinct values in a col
38. nunique() -> gives the count of unqiue values
39. Dealing with DateTimes - 
    a. Converting String formatted dates into date format - 
        1. after loading the data -> pd.to_datetime(col name, format ='%Y-%m-%d %I-%p') -> converts an existing date in string type to Date format mentioned
        2. While loading the data -> 
            df1 = pd.read_csv('data/ETH_1h.csv', parse_dates = ['Date'], date_format = '%Y-%m-%d %I-%p')
    b. df.loc[0, 'Date'].day_name() -> fetches the name of day. But this works for only 1 row not series
    c. df['Date'].dt.day_name() -> this works for a series data and fetches day names for all of the values
    d. We can also apply min and max to get earliest and latest dates. df['Date'].min(). df['Date'].max()
    e. df1['Date'].max() - df1['Date'].min() -> Subtract timestamps
    f. filter data by Dates - 
        1. filt = (df1['Date'] >= '2020')
            df1.loc[filt]
            This filters for all the data for and after 2020
        2. filt = (df1['Date'] >= pd.to_datetime('2019-01-01')) & (df1['Date'] < pd.to_datetime('2020-01-01'))
            We can also use to_datetime format to create filters
        3. df1.loc['2019'] -> This works when 'Date' column set to index
        4. df1['2020-01':'2020-02'] -> filtering between dates
40. "resample" -> groups time-indexed data into new time buckets, then aggregates each bucket. It is groupby for time.
    a. highs = df1['High'].resample('D').max() 
        Here, resample('D') puts all 24hrs of a data into a single day, basically creates groups and then fetches the max value in that group
    b. df1['High'].resample('W').max() -> Resample for week
41. subset.plot() -> pandas default plot method that plots a dataset. This is built using matplotlip, so matplotlip should be installed 
42. Reading different file types -
    a. csv - pd.read_csv('path/file_name')
    b. excel - pd.read_excel('path/file_name')
    c. tsv (tab-separated) -pd.read_csv('path', sep = '\t') 
    d. json - pd.read_json('path/file_name')
    f. urls - pd.read_filetype('url/file_name.filetype')
43. Writing or Creating different file types -
    a. csv - pd.to_csv('path/file_name')
    b. excel - pd.to_excel('path/file_name')
    c. tsv (tab-separated) -pd.to_csv('path/new_file_name', sep = '\t') 
    d. json - pd.to_json('path/file_name')
44. For excel - we need to install these - xlwt openpyxl xlrd
    a. xlwt will write to a file in xls format
    b. xlrd to read excel files
44. Dealing with SQL DBs - 
    a. Install SQLAlchemy and respective DBs. For postgres, it is psycopg2-binary
    b. Create connection -> 
        engine = create_engine('postgresql://user_name:pw@hostname:port/db_name')
    c. Create a SQL table in the DB -> df.to_sql('table_name', engine)
    d. Overwrite an existing table usig 'if_exists' parameter ->
        df.to_sql('sample_table', engine, if_exists = 'replace')
    e. Read an existing table from DB -> sql_df = pd.read_sql('sample_table', engine, index_col = 'Respondent')
    f. Query from a table ->
        sql_df_limit_100 = pd.read_sql_query('select * from sample_table limit 100', engine, index_col = 'Respondent')