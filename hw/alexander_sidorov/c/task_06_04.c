#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "cities.h"


/** -----------------------------------------
My own memory arena
 -------------------------------------------- */
#define MEMSIZE (1<<16)
char arena[MEMSIZE] = {0};
char *memptr = arena;

void *alloc(size_t const amount) {
    char *new_memptr = memptr + amount;
    if (new_memptr > (arena + MEMSIZE - 1)) {
        fprintf(stderr, "memory is depleted");
        exit(-2);
    }
    void *result = (void *) memptr;
    memptr = new_memptr;
    return result;
}

/* ------------------------------------------- */


/**
 * Calculates distance between two geo points
 * @param p0 pointer to geo point
 * @param p1 pointer to geo point
 * @return kilometers
 */
double distance(geo_t const *const p0, geo_t const *const p1) {
    double alat = p0->lat - p1->lat;
    double alon = p0->lon - p1->lon;
    double dlat = alat * ARC_LAT;
    double dlon = alon * ARC_LON;
    double dist = sqrt(dlat * dlat + dlon * dlon);
    return dist;
}


/**
 * Gets the geo point of city by city
 * @param name city city
 * @return bucket (index)
 */
geo_t const *cities_get(const char *const name) {
    int i = 0;
    for (; i < CITIES_LEN; ++i) {
        if (!strcmp(name, CITIES[i].name)) {
            break;
        }
    }

    if (i >= CITIES_LEN) {
        fprintf(stderr, "City with city '%s' not found", name);
        exit(1);
    }

    return &CITIES[i].geo;
}


/**
 * A structure for result of task: {city: distance}
 */
typedef struct {
    char const *city;
    double km_to_center;
} city_distance_t;


/**
 * Calculates the distance from <center> to <city>
 * for each city in CITIES.
 * Creates result as an array of city_distance_t.
 * @param center name of city chosen as a center
 * @return array of city_distance_t
 */
city_distance_t const *distances_to(char const *const center) {
    geo_t const *center_geo = cities_get(center);

    city_distance_t *result = alloc(CITIES_LEN * sizeof(city_distance_t));

    for (int i = 0; i < CITIES_LEN; ++i) {
        city_t* city = &CITIES[i];
        city_distance_t *item = &result[i];

        item->city = city->name;
        item->km_to_center = distance(&city->geo, center_geo);
    }

    return result;
}


int main(int const argc, char const **const argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <center>", argv[0]);
        exit(-3);
    }

    char const *const center = argv[1];

    city_distance_t const *distances = distances_to(center);

    for (int i = 0; i < CITIES_LEN; ++i) {
        city_distance_t const *item = &distances[i];
        printf("%3d  |  %s -> %s: %.2f km\n", i, center, item->city, item->km_to_center);
    }

    return 0;
}
