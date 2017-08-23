package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"math/rand"
)

var grafikmor_sir = []string{
	"ja",
	"nej",
	"mere luft!",
	"hmmmm",
}

func main() {
	fmt.Println("vim-go")
	r := gin.Default()
	r.StaticFile("/favicon.ico", "./resources/favicon.ico")

	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.GET("/sir", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": grafikmor_sir[rand.Intn(len(grafikmor_sir))],
		})
	})
	r.Run()

}
