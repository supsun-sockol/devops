-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: db
-- Время создания: Окт 14 2022 г., 11:50
-- Версия сервера: 8.0.31
-- Версия PHP: 8.0.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `devops`
--

-- --------------------------------------------------------

--
-- Структура таблицы `reps`
--

CREATE TABLE `reps` (
  `id` int NOT NULL,
  `version` mediumtext COLLATE utf8mb4_general_ci NOT NULL,
  `modified` datetime NOT NULL,
  `size` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `reps`
--

INSERT INTO `reps` (`id`, `version`, `modified`, `size`) VALUES
(17, '4.0.0.16', '2022-10-13 13:08:51', 4096),
(18, '3.0.0.166', '2022-10-07 09:00:00', 4096),
(19, '4.0.55555.3235354', '2022-10-10 09:00:00', 4096),
(20, '4.0.0.15', '2022-10-13 13:08:49', 4096),
(21, '4.0.55555.5734898', '2022-10-13 13:08:57', 4096),
(22, '4.0.55555.3832952', '2022-10-13 13:08:55', 4096),
(23, '3.0.0.167', '2022-10-13 13:08:45', 4096);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `reps`
--
ALTER TABLE `reps`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `reps`
--
ALTER TABLE `reps`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
