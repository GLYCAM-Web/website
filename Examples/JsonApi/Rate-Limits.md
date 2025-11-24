# JSON API Rate Limits
After having parts of our website stop working several times, we have implemented rate limits.

_We are thrilled that folks are using the API! Please keep using it!_

These limits should not significantly affect most users.  If your work is limited by them, please consider installing 
[GEMS](https://github.com/GLYCAM-Web/gems).  The JSON I/O is exactly the same, but you run it locally.

## Limits Overview
These limits only apply to `/json/` endpoints, that is, anything like `glycam.org/json/something`.

| Access Type       | Method | Average Limit     | Burst Limit        |
| ----------------- | ------ | ----------------- | ------------------ |
| Service Request   | POST   | 1 per 10 seconds  | 5 per 10 seconds   |
| Information/Other | GET    | 1 per 1 second    | 5 per 1 second     |
| GLYCAM-Web        | _any_  | 1000 per 1 second | 10000 per 1 second |

The limits differ based on the type of access.  Because the site performs bespoke molecular modeling, requests for services require more resources than, 
for example, status updates.

Note that the _Method_ is the defining rule. The method used might not be easy to determine by a casual user. 
### POST Methods
Requests for any new service (sequence build, glyfinder query, etc.), will generally be a POST method. 
### GET Methods
Requesting information or procedural information, for example the status of a service, a CSRF token, etc., then that will generally be a GET method. 
### GLYCAM-Web Access
The last line is necessary because the website initiates services exactly the same way a user would. Status checks and other informational accesses have differences needed by the user interface, but are essentially the same. We do not want to limit access by human users of the site.

## Rate Definitions

### Average
This is the average access rate over an extended time. 
### Burst
This is the number of accesses allowed in any given time period.
### Examples
1. Consider a GET method access:  If you access twice in the first second and then not at all in the second second and then continue that pattern, you will not hit rate limits because you are maintaining an average of 1 access per second.
2. Still considering the GET method: Of course, you might say "ok, I'll ask for 10,000 status queries and then not ask again for 10,000 seconds". This is why the _burst_ limit is there. This is the maximum number of accesses all at once (within a very short time). If you ask for more than 5 GET methods in a second, the site will limit access until the average access falls under 1 per second.
### CSRF Tokens
These count toward your rate limit. Note that you do not need a new CSRF token for every access of the JSON API (TEST ME!!!).

## Implementation Method

Sample files relevant to our rate limit implementation via interaction of [Docker Swarm](https://docs.docker.com/engine/swarm/) and [Traefik](https://traefik.io/traefik) can be viewed [here](https://github.com/GLYCAM-Web/GLYCAM_Traefik_V3_Proxy/blob/main/Examples/docker-compose.proxy.swarm.traefik.ratelimits.yml). 

The rules are applied in this order:
1. For `/json/` endpoints served by any of our websites:
	1. If the `Referer` is the website host for the `/json/` endpoint, then the limits for the `GLYCAM-Web` access are applied.
	2. If not, and if the `METHOD` is `POST`, the limits for `Service Request` are applied.
	3. ...if the `METHOD` is `GET`, the limits for `Information/Other` are applied.
2. All other access is treated as normal website traffic.

