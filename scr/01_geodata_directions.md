# 01 geodata exploration

## Explore directions of from_to formula

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
  mutate(top_list = paste0(type_pair, collapse = " <br> ")) %>% 
  select(-n, -type_pair) %>% 
  ungroup() %>% 
  distinct() %>% 
  #pivot_wider(names_from = lang, values_from = top_list) %>% 
  knitr::kable(escape = F)
```

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;" data-quarto-table-cell-role="th">lang</th>
<th style="text-align: left;"
data-quarto-table-cell-role="th">top_list</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">cs</td>
<td style="text-align: left;">default --&gt; default (128)<br />
mountain --&gt; mountain (50)<br />
river --&gt; river (25)<br />
river --&gt; default (20)<br />
mountain --&gt; default (19)</td>
</tr>
<tr class="even">
<td style="text-align: left;">de</td>
<td style="text-align: left;">default --&gt; default (43)<br />
river --&gt; river (8)<br />
default --&gt; river (3)<br />
country --&gt; country (2)<br />
default --&gt; country (2)</td>
</tr>
<tr class="odd">
<td style="text-align: left;">en</td>
<td style="text-align: left;">default --&gt; default (182)<br />
default --&gt; country (23)<br />
default --&gt; river (20)<br />
river --&gt; river (20)<br />
country --&gt; country (16)</td>
</tr>
<tr class="even">
<td style="text-align: left;">fr</td>
<td style="text-align: left;">default --&gt; default (199)<br />
river --&gt; river (30)<br />
river --&gt; default (13)<br />
country --&gt; default (12)<br />
default --&gt; country (12)</td>
</tr>
<tr class="odd">
<td style="text-align: left;">it</td>
<td style="text-align: left;">default --&gt; default (12)<br />
mountain --&gt; default (4)<br />
default --&gt; river (2)<br />
river --&gt; default (2)<br />
river --&gt; river (2)</td>
</tr>
<tr class="even">
<td style="text-align: left;">ru</td>
<td style="text-align: left;">default --&gt; default (93)<br />
river --&gt; default (20)<br />
river --&gt; river (19)<br />
default --&gt; river (14)<br />
country --&gt; default (9)</td>
</tr>
<tr class="odd">
<td style="text-align: left;">sl</td>
<td style="text-align: left;">default --&gt; default (16)<br />
default --&gt; mountain (2)<br />
mountain --&gt; sea (2)<br />
river --&gt; default (2)<br />
default --&gt; river (1)<br />
river --&gt; river (1)</td>
</tr>
</tbody>
</table>
