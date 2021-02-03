/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2020 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "adc.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
uint8_t RX_Buff[20];
uint16_t ADCValueFront, ADCValueLeft, tekst;
uint8_t RUN = 1, RUN2 = 0;
uint16_t krok = 19891/4, skret90 = 5646/4, preskaler = 5000/4, sygnal = 3100;
uint8_t tablica[40] = {0};
uint8_t pos = 1, pom1, pom2, pom3, pom4, pom5, pom6, pom7, pom8, pom9, pom10;
uint8_t skandal[40];

int i;
char dzialanie, trasa, koniec;
uint8_t przycisk = 0;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */
void jazdaPrzod( uint16_t Tim, uint16_t Pr1, uint16_t Pr2);
void jazdaPrawo( uint16_t Tim);
void jazdaLewo( uint16_t Tim);
void pomiar(void);

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */
  

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART2_UART_Init();
  MX_TIM3_Init();
  MX_TIM1_Init();
  MX_ADC1_Init();
  MX_ADC2_Init();
  MX_USART1_UART_Init();
  /* USER CODE BEGIN 2 */
  huart2 = huart1;
//while(1){
  //pomiar();
//}
HAL_Delay(12000);
  /* USER CODE END 2 */
  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
	  pomiar();
	  	  if (RUN == 1){
	  		    if(ADCValueLeft < sygnal && ADCValueFront > sygnal)
	  		    {

	  		    						dzialanie = 'F';
										tablica[pos -1] = dzialanie;
										dzialanie = 0;
										jazdaPrzod(krok,preskaler,preskaler);
										RUN = 1;}

	  		    }
	  		    else if(ADCValueFront > sygnal && ADCValueLeft > sygnal)
	  		    {
	  		    	dzialanie = 'L';
	  		    	tablica[pos -1] = dzialanie;
	  		    	dzialanie = 0;
	  		    	jazdaLewo(skret90+15);
	  		    	HAL_Delay(500);
	  		    	jazdaPrzod(krok, preskaler, preskaler);
	  		    	RUN = 1;
	  		    }
	  		    else if (ADCValueFront < sygnal && ADCValueLeft > sygnal){

	  		    	dzialanie = 'L';
	  		    	tablica[pos -1] = dzialanie;
	  		    	dzialanie = 0;
	  		    	jazdaLewo(skret90+15);
	  		    	HAL_Delay(500);
	  		    	jazdaPrzod(krok, preskaler, preskaler);
	  		    	RUN = 1;
	  		    }
	  		    else if(ADCValueLeft < sygnal  && ADCValueFront < sygnal)
	  		    {
	  		    	dzialanie = 'R';
	  		    	tablica[pos -1] = dzialanie;
	  		    	dzialanie = 0;
	  		    	jazdaPrawo(skret90);
	  		    	RUN = 1;
	  		    }
	  		    else {
	  		    	jazdaLewo(1000);
	  		    	jazdaPrawo(1000);
	  		    	jazdaLewo(1000);
	  		    	dzialanie = 'K';
	  		    	tablica[pos -1] = dzialanie;
	  		    	dzialanie = 0;
	  		    	RUN = 0;
	  		    }


	  		    pomiar();

	  		    pos = pos +1 ;
	  		    HAL_UART_Receive(&huart2, (uint8_t *)&koniec, 1, 1000);

	  		    if (koniec == '1') {
	  		    	tablica[pos -1] = 'K';
	  		    	HAL_UART_Transmit(&huart2, (uint8_t*)tablica, sizeof(tablica), 1000);
	  		    	jazdaLewo(2000);
	  		    	jazdaPrawo(4000);
	  		    	jazdaLewo(2000);
	  		    	RUN = 0;
	  		    	RUN2 = 1;
	  		  }

	  		    HAL_Delay(500);
	  		    }
	  	  if (RUN2 == 1){

	  		    if (HAL_UART_Receive(&huart2, (uint8_t*)skandal, 40, 10000) == HAL_OK){
	  		    	jazdaLewo(skret90*2);
	  		    	for (i=0; i<sizeof(skandal); i++){
	  		    		if (skandal[i] == 'F'){
	  		    			jazdaPrzod(krok, preskaler, preskaler);


	  		    	}	if (skandal[i] == 'R'){
	  		    			jazdaPrawo(skret90);
	  		    			jazdaPrzod(krok, preskaler, preskaler);

	  		    	}	if (skandal[i] == 'L'){
	  		    			jazdaLewo(skret90);
	  		    			jazdaPrzod(krok, preskaler, preskaler);



	  		    	}	if (skandal[i] == 'K') {
	  		    			jazdaLewo(skret90/2);
	  		    			jazdaPrawo(skret90);
	  		    			jazdaLewo(skret90/2);
	  		    			RUN2 = 0;
	  		    	}
	  		    }
	  		    }
	  		    }







    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  /** Initializes the CPU, AHB and APB busses clocks 
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_BYPASS;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV2;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL15;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB busses clocks 
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_ADC;
  PeriphClkInit.AdcClockSelection = RCC_ADCPCLK2_DIV6;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */

void pomiar(void)
{

  HAL_ADC_Start(&hadc1);
	  if(HAL_ADC_PollForConversion(&hadc1,1) == HAL_OK)
		  {
			  ADCValueFront = HAL_ADC_GetValue(&hadc1);
		  }
	  HAL_ADC_Start(&hadc2);
	  		  if(HAL_ADC_PollForConversion(&hadc2,1)== HAL_OK)
	  		 {
	  			  ADCValueLeft = HAL_ADC_GetValue(&hadc2);


	  		}
}


void jazdaPrzod( uint16_t Tim, uint16_t Pr1, uint16_t Pr2)
{
	  HAL_TIM_PWM_Stop(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Stop(&htim3,TIM_CHANNEL_3);

	  HAL_GPIO_WritePin(en1_GPIO_Port, en1_Pin, GPIO_PIN_RESET);
	  HAL_GPIO_WritePin(en2_GPIO_Port, en2_Pin, GPIO_PIN_RESET);

	  HAL_GPIO_WritePin(Dir_motor1_GPIO_Port, Dir_motor1_Pin, GPIO_PIN_RESET);
	  HAL_GPIO_WritePin(Dir_motor2_GPIO_Port, Dir_motor2_Pin, GPIO_PIN_SET);
	  __HAL_TIM_SET_PRESCALER(&htim1, Pr1);
	  __HAL_TIM_SET_PRESCALER(&htim3, Pr2);


	  HAL_TIM_PWM_Start(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Start(&htim3,TIM_CHANNEL_3);



	  HAL_Delay(Tim);


	  HAL_TIM_PWM_Stop(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Stop(&htim3,TIM_CHANNEL_3);

}

void jazdaLewo( uint16_t Tim)
{

	  HAL_TIM_PWM_Stop(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Stop(&htim3,TIM_CHANNEL_3);

	  HAL_GPIO_WritePin(en1_GPIO_Port, en1_Pin, GPIO_PIN_RESET);
	  HAL_GPIO_WritePin(en2_GPIO_Port, en2_Pin, GPIO_PIN_RESET);

	  HAL_GPIO_WritePin(Dir_motor1_GPIO_Port, Dir_motor1_Pin, GPIO_PIN_SET);
	  HAL_GPIO_WritePin(Dir_motor2_GPIO_Port, Dir_motor2_Pin, GPIO_PIN_SET);
	  __HAL_TIM_SET_PRESCALER(&htim1, preskaler);
	  __HAL_TIM_SET_PRESCALER(&htim3, preskaler);
	  HAL_TIM_PWM_Start(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Start(&htim3,TIM_CHANNEL_3);

	  HAL_Delay(Tim);
	  HAL_TIM_PWM_Stop(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Stop(&htim3,TIM_CHANNEL_3);


}

void jazdaPrawo( uint16_t Tim)
{

	  HAL_TIM_PWM_Stop(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Stop(&htim3,TIM_CHANNEL_3);

	  HAL_GPIO_WritePin(en1_GPIO_Port, en1_Pin, GPIO_PIN_RESET);
	  HAL_GPIO_WritePin(en2_GPIO_Port, en2_Pin, GPIO_PIN_RESET);

	  HAL_GPIO_WritePin(Dir_motor1_GPIO_Port, Dir_motor1_Pin, GPIO_PIN_RESET);
	  HAL_GPIO_WritePin(Dir_motor2_GPIO_Port, Dir_motor2_Pin, GPIO_PIN_RESET);
	  __HAL_TIM_SET_PRESCALER(&htim1, preskaler);
	  __HAL_TIM_SET_PRESCALER(&htim3, preskaler);
	  HAL_TIM_PWM_Start(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Start(&htim3,TIM_CHANNEL_3);

	  HAL_Delay(Tim);
	  HAL_TIM_PWM_Stop(&htim1,TIM_CHANNEL_1);
	  HAL_TIM_PWM_Stop(&htim3,TIM_CHANNEL_3);



}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{ 
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
