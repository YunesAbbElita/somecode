#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modulos
import pygame

######################## FUNCIONES ###########################
# ---------------------------------------------------------- #

def load_level(op): # Funcion que define los mapas y selecciona el elegido
  if op == 1:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW      WWWWWWWWWWWWWWWWWWWWWWWWWWW            W",
    "W              WWW      WWW                     WWW            W",
    "W              WWW                              WWW         O  W",
    "W              WWW                              WWWWWWWWWWWWWWWW",
    "W              WWW                                             W",
    "WWWWWWWWW      WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                     W                       W",
    "W              WWW                     W                       W",
    "W              WWW         E           W                       W", 
    "W              WWWWWWWWWWWWWWWWWWWWWWWWW                       W",
    "W                                    WWW                       W",
    "W                                    WWW                       W",
    "W                                    WWW                       W",
    "W                                    WWW                       W",
    "W                                    WWW                       W",
    "W                                    WWW                       W",
    "W                                    WWW                       W",
    "W                                    WWW                       W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW          WWW                       W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "WT                                   E                      S  W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
  elif op==2:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWW                                             W",
    "W              WWWO               E       WWWWWWWWWw           W",
    "W              WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                  W",
    "W              WWW                        WWW                  W",
    "W              WWW                        WWW                  W",
    "W     S        WWW                        WWW                  W",
    "WWWWWWWWW      WWW                        WWW                  W",
    "W              WWW                        WWW                  W",
    "W              WWW                        WWW                  W",
    "W              WWW                        WWW                  W",
    "W              WWW           T            WWW       WWWWWWWWWWWW",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWW                  W",
    "W              WWW           WWW          WWWWWWWWWWWWW        W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "W                            WWW                               W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
  elif op==3:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W            WWW                                               W",
    "W            WWW                                               W",
    "W            WWW                                               W",
    "W            WWW                                               W",
    "W            WWW                                               W",
    "W            WWW                                               W",
    "W            WWW            S                                  W",
    "W            WWWWWW     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      W",
    "W            WWW                                      WWW      W",
    "W            WWW                                      WWW      W",
    "W            WWW                                      WWW      W",
    "W            WWW                                      WWW      W",
    "W            WWW                                      WWW      W",
    "W            WWW                                      WWW      W",
    "W            WWW                                      WWW      W",
    "W            WWW                          WWWWWWWWWWWWWWW      W",
    "W            WWWWWWWWWWWWWWWWWW           WWW                  W",
    "W            WWW                          WWW                  W",
    "W            WWW                          WWW                  W",
    "W            WWW                          WWW         WWWWWWWWWW",
    "W            WWW                          WWW         WWWO  O  W",
    "W            WWW                          WWW         WWW      W",
    "W            WWW                          WWW         WWW      W",
    "W            WWW                          WWW         WWW      W",
    "W            WWW                          WWW         WWW      W",
    "W            WWW                 E     T  WWW         WWW      W",
    "W            WWWWW     WWWWWWWWWWWWWWWWWWWWWWWW     WWWWW      W",
    "W                               WWW                   WWW      W",
    "W                               WWW                   WWW      W",
    "W                               WWW                   WWW      W",
    "W                               WWW                   WWW      W",
    "W                               WWW                   WWW      W",
    "W                               WWW                   WWW      W",
    "W                               WWW                            W",
    "W                               WWW                            W",
    "W                               WWW                            W",
    "W                               WWW                            W",
    "W               E               WWW                            W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    ]
  elif op==4:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W              WWWWWWWWWWWWWWWWWWWWWW                       WWWW",
    "W                WWWWWWWWWWWWWWWWW                             W",
    "W                   WWWWWWWWWWWW                               W",
    "W                      WWWWWWWW                                W",
    "W                         WWWWW                                W",
    "W                           WWW                        O       W",
    "W                           WWW              WWWWWWWWWWWWWWWWWWW",
    "W                           WWW                     WWWWWWWWWWWW",
    "W                           WWW                          WWWWWWW",
    "WWWWWWW                     WWWW                            WWWW",
    "WWWWWWWWWWW                 WWWWWW                            WW",
    "WWWWWWWWWWWWW                 WWWWWW                          WW",
    "WWWWWWWWWWWWWWW                 WWWWWW                        WW",
    "WWWWWWWWWWWWWWWWW                 WWWWWWW                      W",
    "WWWWWWWWWWWWWWWWWWW                 WWWWWW                     W",
    "WWWWWWWWWWWWWWWWWWWWW                 WWWWWWWW                 W",
    "WWWWWWWWW           WWW                 WWWWWWWW               W",
    "WWWWW                 WWW                 WWWWWWW              W",
    "WW                      WWW                 WWWWW      E       W", 
    "W                         WWW                 WWW              W",
    "W                           WWW               WWW              W",
    "W                           WWW               WWW              W",
    "W                           WWW               WWW              W",
    "W                                             WWW              W",
    "W                                             WWW      E       W",
    "W      E      W                               WWW              W",
    "W             WWW                             WWW              W",
    "W             WWWWW                         WWW                W",
    "WT            WWWWWWW                     WWW               S  W",
    "W             WWWWWWWWW                 WWW                    W",
    "W      E      WWWWWWWWWWWWWWWWWWWWWWWWWWWW             E       W",
    "W                                                              W",
    "W                                                             WW",
    "W                                                             WW",
    "W                                                             WW",
    "W                                                            WWW",
    "WWW                                                       WWWWWW",
    "WWWWWWWW                                             WWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
  elif op == 5:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W           WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                WWWWWWWWWWWWWWW",
    "W                                                             WW",
    "W                                                             WW",
    "W                                                             WW",
    "W                                                WWWWWWWWWW   WW",
    "W                                               WWWWWWWWWWW   WW",
    "W           WWWWWWWWWWWWWWWW                    WWWWWWWWWWW   WW",
    "W           WWWWWWWWWWWWWWWW                    WWWWWWWWWWW   WW",
    "W           WWWWWWWWWWWWWWWWWWW                   WWWWWWWWW   WW",
    "W           WWWWWWWWWWWWWWWWWWW                   WWWWWWWWW   WW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                   WWWWWWWWW   WW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW         E         WWWWWWWWW   WW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                   WWWWWWWWW   WW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                   WWWWWWWWW   WW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWW                      WWWWWWWWW   WW",
    "WWWWWWWWWWWW                                      WWWWWWWWW   WW",
    "WWWWWWWWWWWW                                 WWWWWWWWWWWWWW   WW",
    "WWWWWWWWWWWW                                 WWWWWWWWWWWWWW   WW",
    "WWWWWWW                                WWWWWWWWWWWWWWWWWWWW   WW",
    "WWWWWWW                           S    WWWWWWWWWWWWWWWWWWWW   WW",
    "WWWWWWW                  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   WW",
    "WWW                      WWWWWWWWWWW                WWWWWWW   WW",
    "WW                  WWWWW      T                     WWWWWW   WW",
    "W                 WWWWWWW                             WWWWW   WW",
    "W                 WWW                                  WWWW   WW",
    "W                 WWW                                   WWW   WW",
    "W     E           WWW                                    WW   WW",
    "WW                WWW     E             W                 W   WW",
    "WWW               WWWWWW                WWW                   WW",
    "WWWW                                    WWWWW                 WW",
    "WWWWW                                   WWWWWW                WW",
    "WWWWWW                                  WWWWWWW               WW",
    "WWWWWWW                                 WWWWWWWW              WW",
    "WWWWWWWW                                WWWWWWWWW             WW",
    "WWWWWWWWW                               WWWWWWWWW             WW",
    "WWWWWWWWWW                              WWWWWWWWW             WW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      O      WW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
  elif op == 6:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                               W         W          WWWWWWWWWWW",
    "W                             W        W         W        WWWWWW",
    "W                        W                            W     WWWW",
    "W                                 W    W     W                WW",
    "W                                   W    W         W          WW",
    "W                                                              W",
    "W                                       W    W                 W",
    "W                                                              W",
    "W  W       W                                                   W",
    "W                                        W      E              W",
    "W   W   W                              W               W       W",
    "W                                   W                W         W",
    "W  W    W                        W                         O   W",
    "W                          W        W                   WWWWWWWW",
    "W                                                              W",
    "W  W  W                 W         W               W   W        W",
    "W                                                              W",
    "W                            W                            W    W",
    "W  W      W                                        W           W",
    "W                               W      E               W       W",
    "W     W     W                                   W              W",
    "W                          W                                   W",
    "W      W                                                  W    W",
    "W                         W    W                     W         W",
    "W  W                                                           W",
    "W        W                                       W             W",
    "W    W                   W                            W    W   W",
    "W  W                                                           W",
    "W           E                                       W          W",
    "W    W                  W                     W                W",
    "W                                      W                       W",
    "WW                                                      W  S   W",
    "WW                                               W         W  WW",
    "WW   W                                   W             W      WW",
    "WWW                                W   W                     WWW",
    "WWWWW                 W                   W    W          WWWWWW",
    "WWWWWWWWT           W     W          W                  WWWWWWWW",
    "WWWWWWWWWWWW     W                                  WWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
  elif op == 7:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                              W",
    "W                                                              W",
    "W        E                    E                      E         W",
    "W                                                              W",
    "W              W                                            S  W",
    "W              W                                               W",
    "W              W                                               W",
    "W                                                              W",
    "W                                                              W",
    "W              E              E              E                 W",
    "W                                                              W",
    "W                                                              W",
    "W                                            W                 W",
    "W                                            W                 W",
    "W                                            W                 W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W        E                    E                      E         W",
    "W                                                              W",
    "W                                                              W",
    "W              W                                               W",
    "W              W                                               W",
    "W              W                                               W",
    "W                                                              W",
    "W                                                              W",
    "W              E              E              E                 W",
    "W                                                              W",
    "W                                                              W",
    "W                                            W                 W",
    "W                                            W                 W",
    "W                                            W                 W",
    "W                                                              W",
    "W                                                              W",
    "W        E                    E                      E         W",
    "W                                                              W",
    "W                                                              W",
    "WT                                                  O          W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
  elif op == 8:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                WWWWWWWWWWWWWWW                               W",
    "W               WWWWWWWWWWWWWWWW                               W",
    "W              WWWWWWWWWWWWWWWWW                               W",
    "W             WWWWWWWWWWWWWWWWWW                 W             W",
    "W            WWWWWWWWWWWW                        W             W",
    "W           WWWWWWWWWWWWW                        W E           W",
    "W           WWWWW                                W             W",
    "W           WWWWW                                W             W",
    "W           WWWWW                                W             W",
    "W           WWWWW                                W             W",
    "W           WWWWW           WWWWWWWWWWWWWWWWWWWWWW             W",
    "W           WWWWW           WWWWWWWWWWWWWWWWWWWWWW             W",
    "W           WWWWW           WW                   W             W",
    "W           WWW         WWWWWW                   W             W",
    "W           WWW         W                        W             W",
    "W           WWW         W                        W             W",
    "W           WWW         W                        W             W",
    "W           WWW         W          WWWWW         W             W",
    "W           WWW         W              W         WTE           W",
    "W           WWW         W              W         WWWWWWWW      W",
    "W          WWWW         W              W         WWWWWWW       W",
    "W         WWWW          W              W         WWWWWW        W",
    "W        WWWW           WW     O     WW          WWWWW         W",
    "W       WWWW             WWWWWWWWWWWWW           WWWW          W",
    "W       WWWW                                     WWW           W",
    "W       WWWW                                     WW            W",
    "W       WWWW                                     W             W",
    "W       WWWW                                S    W             W",
    "W       WWWW                               WWWWWWW             W",
    "W       WWWW                               WWWWWWW             W",
    "W        WWWW                              WWWWWWW             W",
    "W         WWWW                             WWWWWWW             W",
    "W          WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW E           W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
  elif op == 9:
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "WWWWWWWWWW      WWWWWWWWWWWW      WWW      WWW      WWW      WWW",
    "WWWWWWWWWWWWWWWWWWW      WWW      WWW      WWW      WWW      WWW",
    "W                                                             WW",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                            E                                 W",
    "W                                                              W",
    "W S                                                            W",
    "WWWWW      WWW      WWW      WWWWWWWWWWWWWWWWWWWWW      WWW    W",
    "WWWWW      WWW      WWW      WWW      WWW      WWW      WWW    W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                            E                                 W",
    "W                                                              W",
    "W                                                           T  W",
    "WW     WWW      WWWWWWWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWWWWWWW",
    "WW     WWW      WWW      WWW      WWWWWWWWWWWW      WWWWWWWWWWWW",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                            E                                 W",
    "W                                                              W",
    "W                                                              W",
    "WWWWW      WWW      WWW      WWW      WWW      WWW             W",
    "WWWWW      WWW      WWW      WWW      WWW      WWW             W",
    "WWWWW      WWW      WWW      WWW      WWW      WWW      O      W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

  return level # devuelve el nivel elegido

def init_level(level,Wall,Enemy): # Esta funcion recibe el nivel elegido y lo carga en las listas
  x = y = 0
  tele = [0,0]
  
  for row in level:
    for col in row:
      if col == "W":
        Wall((x, y)) # llamo a la clase wall y le mando las cordenadas x,y del muro, cada "W" es un muro diferente
      if col == "E":
        Enemy((x, y-32)) # lo mismo que pero con enemigos
      if col == "O":
        end_rect = pygame.Rect(x, y, 48, 16) # cargo el rectangulo de salida
      if col == "T":
        teleport_rect = pygame.Rect(x, y, 48, 16) # cargo el rectangulo de teleport
      if col == "S": # con esto cargo las cordenadas de salida del teleport
        tele[0] = x
        tele[1] = y
      x += 16
    y += 16
    x = 0
    
  return end_rect, teleport_rect, tele # devuelve salida, teleport y las cordenadas de salida del teleport