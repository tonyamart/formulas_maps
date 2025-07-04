# 01_geodata_directions

## Explore directions of from_to formula

``` r
library(tidyverse)
```

    ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
    ✔ dplyr     1.1.4     ✔ readr     2.1.4
    ✔ forcats   1.0.0     ✔ stringr   1.5.1
    ✔ ggplot2   3.5.1     ✔ tibble    3.3.0
    ✔ lubridate 1.9.3     ✔ tidyr     1.3.1
    ✔ purrr     1.0.4     
    ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ✖ dplyr::filter() masks stats::filter()
    ✖ dplyr::lag()    masks stats::lag()
    ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

Read data as a table

``` r
formulas <- read.csv("../data/formulas_table.csv")
glimpse(formulas)
```

    Rows: 1,255
    Columns: 14
    $ lang           <chr> "cs", "cs", "cs", "cs", "cs", "cs", "cs", "cs", "cs", "…
    $ doc_key        <chr> "0001_0001-0001-0000-0008-0000", "0036_0001-0000-0000-0…
    $ triplet_id     <int> 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1…
    $ from_id        <chr> "Q1497", "Q584", "Q1410", "Q155975", "Q155975", "Q545",…
    $ to_id          <chr> "Q668", "Q545", "Q545", "Q1887287", "Q1085", "Q13924", …
    $ text           <chr> "od břehů širých otce Missisipi až k Indu", "od Pyramid…
    $ from_placename <chr> "Mississippi River", "Rhine", "Gibraltar", "Kutná Hora"…
    $ from_type      <chr> "default", "river", "default", "default", "default", "d…
    $ from_latitude  <dbl> 29.15360, 47.66620, 36.14000, 49.94844, 49.94844, 58.00…
    $ from_longitude <dbl> -89.250800, 9.178600, -5.350000, 15.268226, 15.268226, …
    $ to_placename   <chr> "India", "Baltic Sea", "Baltic Sea", "Malešov", "Prague…
    $ to_type        <chr> "country", "default", "default", "default", "default", …
    $ to_latitude    <dbl> 22.80000, 58.00000, 58.00000, 49.91107, 50.08750, 42.77…
    $ to_longitude   <dbl> 83.00000, 20.00000, 20.00000, 15.22440, 14.42139, 15.42…

### types

total

``` r
formulas %>% 
  mutate(type_pair = paste0(from_type, " --> ", to_type)) %>% 
  count(type_pair, sort = T)
```

                     type_pair   n
    1      default --> default 673
    2          river --> river 105
    3        river --> default  72
    4    mountain --> mountain  63
    5      default --> country  58
    6        default --> river  58
    7     mountain --> default  44
    8      country --> default  42
    9     default --> mountain  34
    10     country --> country  30
    11      mountain --> river  13
    12         default --> sea   8
    13      river --> mountain   8
    14        mountain --> sea   6
    15    mountain --> country   4
    16 continent --> continent   3
    17   continent --> default   3
    18       country --> river   3
    19   default --> continent   3
    20  mountain --> continent   3
    21       river --> country   3
    22         sea --> country   3
    23    country --> mountain   2
    24         country --> sea   2
    25           river --> sea   2
    26        sea --> mountain   2
    27           sea --> river   2
    28   continent --> country   1
    29     continent --> river   1
    30   country --> continent   1
    31     river --> continent   1
    32       sea --> continent   1
    33         sea --> default   1

by language

``` r
formulas %>% 
  mutate(type_pair = paste0(from_type, " --> ", to_type)) %>% 
  group_by(lang) %>% 
  count(type_pair, sort = T) %>% 
  slice_max(order_by = n, n = 5) %>% 
  ungroup() %>% 
  mutate(type_pair = paste0(type_pair, " (", n, ")")) %>% 
  group_by(lang) %>% 
  mutate(top_list = paste0(type_pair, collapse = " \n ")) %>% 
  select(-n, -type_pair) %>% 
  ungroup() %>% 
  distinct() %>% 
  pivot_wider(names_from = lang, values_from = top_list)
```

    # A tibble: 1 × 7
      cs                                         de    en    fr    it    ru    sl   
      <chr>                                      <chr> <chr> <chr> <chr> <chr> <chr>
    1 "default --> default (128) \n mountain --… "def… "def… "def… "def… "def… "def…
