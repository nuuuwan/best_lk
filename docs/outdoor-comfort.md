# What the outdoor comfort score measures

For someone deciding where to live, one concrete question is how often the weather suits a walk. The score estimates the share of daytime hours that were both dry and thermally mild for a person walking in shade. A score of 25% means about three of the twelve assessed hours per day on average. Those hours can be spread across different days.

## What the research supports

**Heat, humidity and wind act together.** At the same dew point, a cooler morning and a hotter afternoon can feel quite different. Moving air changes how the body loses heat. Bröde and colleagues developed the Universal Thermal Climate Index (UTCI) by modelling the response of a person walking outdoors to air temperature, moisture, wind and radiant heat, with clothing adapting to the weather. Its equivalent temperature gives us a consistent way to compare a coastal town with a highland town. [Original UTCI methods paper](https://doi.org/10.1007/s00484-011-0454-1)

**Exposure matters within the same city.** In Colombo, Johansson found that choosing the shaded side of a street could substantially reduce daytime heat exposure. Direct sun and heat radiating from sunlit surfaces both contributed. The maps therefore describe one explicit scenario, walking in shade. We approximate it by setting mean radiant temperature equal to air temperature at each hour. A sunlit road or a hot wall can feel considerably warmer. [Colombo field measurements and street simulations, chapter 6](https://lucris.lub.lu.se/ws/portalfiles/portal/4643420/547096.pdf)

**Thermal stress and personal preference answer different questions.** Simath and Emmanuel analysed records from 20 Sri Lankan weather stations and used UTCI categories to compare heat stress across the island. They explicitly identified local calibration as a limitation. In a tropical park in Singapore, a survey of 1,508 visitors found that preferred, neutral and acceptable conditions differed, and acclimatisation mattered. That survey used a different index, Physiologically Equivalent Temperature. Its numerical limits cannot be transferred directly to UTCI. For this map the standard UTCI band provides a repeatable benchmark. A resident who enjoys warmer weather may find many more hours pleasant. [Sri Lankan station study](https://doi.org/10.1007/s00484-022-02328-9) · [Tropical park survey](https://doi.org/10.1007/s00484-019-01694-1)

## How a location earns its score

| Choice | Definition and rationale |
| --- | --- |
| Time window | Twelve hourly readings from 07:00 through 18:00 Sri Lanka time, on each of the previous 365 complete days. This fixed daytime window is a project choice for comparing outdoor activity. |
| Thermal criterion | UTCI above 9 °C and at or below 26 °C, the published no-thermal-stress band. This includes a lower limit for cool highland conditions. |
| Rain criterion | Less than 0.1 mm in the hour ending at the reading. This project preference describes a practically dry walk. A downpour in the evening no longer disqualifies a dry morning. |
| Calculation | Divide the count of hours meeting both criteria by the number with usable data, then multiply by 100. Missing hours contribute to neither count. A fully covered year has 4,380 hours. |
| Weather inputs | Use simultaneous air temperature and dew point at 2 m and wind at 10 m. ECMWF’s thermofeel evaluates the UTCI polynomial in Kelvin. Use a 0.5 m/s wind floor for calm conditions and exclude wind above 17 m/s and temperatures outside −50 to 50 °C. |

The UTCI band comes from the physiological model. The rain cutoff and daytime window express a preference about when to go outside. The earlier rule counted whole days with maximum dew point below 23 °C and rainfall below 10 mm. Percentages from those two definitions have different denominators. [ECMWF threshold definitions](https://confluence.ecmwf.int/pages/viewpage.action?pageId=473828332) · [ECMWF thermofeel calculation](https://thermofeel.readthedocs.io/en/latest/guide/utci.html) · [Open-Meteo archive variables](https://open-meteo.com/en/docs/historical-weather-api)

## Interpreting the maps

The national and Greater Colombo maps use identical thresholds and a common 0–100% colour scale. Each point uses weather from the archive grid at that location. Nearby suburbs can share a grid cell. Trees, street orientation, sea-breeze exposure and shelter can all matter within one cell, so small differences between suburbs deserve little weight. A single year also captures that year's monsoons. Longer records would be needed to describe typical conditions over decades. [Open-Meteo model resolution](https://open-meteo.com/en/docs/historical-weather-api) · [Colombo urban shading study](https://doi.org/10.1002/joc.1609)

## What changed in the 2025–26 comparison

For 20 November 2025 through 19 November 2026, these three sites had complete coverage under both definitions. The old rule could exclude a full day because of a single muggy hour. It could also admit a hot, dry afternoon. The hourly score gives each usable hour equal weight and can distinguish both cases.

| Location | Days meeting the former rule | Dry daytime hours in the shaded UTCI band |
| --- | ---: | ---: |
| Nuwara Eliya | 285 / 365 (78.1%) | 1,813 / 4,380 (41.4%) |
| Kandy | 240 / 365 (65.8%) | 1,074 / 4,380 (24.5%) |
| Colombo | 38 / 365 (10.4%) | 220 / 4,380 (5.0%) |

These are two descriptions of the same year's weather. The difference between the percentages reflects the change of question and denominator.
