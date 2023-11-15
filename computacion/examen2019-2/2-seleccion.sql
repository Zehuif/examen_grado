CREATE TABLE "public"."SELECCION" (
  "id_seleccion" varchar(255) NOT NULL,
  "id_personaje" varchar(255),
  "id_partido" varchar(255),
  "id_jugador" varchar(255),
  PRIMARY KEY ("id_seleccion"),
  CONSTRAINT "id_jugador" FOREIGN KEY ("id_jugador") REFERENCES "public"."JUGADOR" ("id_jugador"),
  CONSTRAINT "id_partido" FOREIGN KEY ("id_partido") REFERENCES "public"."PARTIDO" ("id_partido"),
  CONSTRAINT "id_personaje" FOREIGN KEY ("id_personaje") REFERENCES "public"."PERSONAJE" ("id_personaje")
)
;