CREATE UNLOGGED TABLE people (
    id serial PRIMARY KEY,
    name text NOT NULL,
    domain text NOT NULL,
    countryCode text NOT NULL,
    longitude float,
    latitude float,
    pageViewsEnglish bigint,
    birthYear smallint,
    birthState text,
    occupation text NOT NULL,
    en_curid int NOT NULL,
    numLangs smallint,
    birthCity text,
    averageViews float,
    totalPageViews int,
    countryName text NOT NULL,
    stdDevPageViews float,
    countryCode3 text NOT NULL,
    pageViewsNonEnglish int,
    dataset text NOT NULL,
    l_star float,
    gender text NOT NULL,
    industry text NOT NULL,
    hpi float,
    continentName text NOT NULL
);