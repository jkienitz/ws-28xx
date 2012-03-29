#!/usr/bin/python

import time
import logging
import USBHardware
import CWeatherTraits

CWeatherTraits = CWeatherTraits.CWeatherTraits()
USBHardware = USBHardware.USBHardware()

class CCurrentWeatherData(object):
	_PressureRelative_hPa = 0
	_PressureRelative_hPaMinMax = 0
	_PressureRelative_inHg = 0
	_WindSpeed = 0
	_WindDirection = 16
	_WindDirection1 = 16
	_WindDirection2 = 16
	_WindDirection3 = 16
	_WindDirection4 = 16
	_WindDirection5 = 16
	_Gust = 0
	_GustDirection = 16
	_GustDirection1 = 16
	_GustDirection2 = 16
	_GustDirection3 = 16
	_GustDirection4 = 16
	_GustDirection5 = 16
	_Rain1H =0
	_Rain24H =0
	_RainLastWeek =0
	_RainLastMonth =0
	_RainTotal =0
	_IndoorTemp =0
	_OutdoorTemp =0
	_IndoorHumidity =0
	_OutdoorHumidity =0
	_Dewpoint =0
	_Windchill =0
	_WeatherState = 3
	_WeatherTendency = 3
	_AlarmRingingFlags = 0
	_AlarmMarkedFlags = 0

	def __init__(self):
		self.logger = logging.getLogger('ws28xx.CCurrentWeatherData')

	def CCurrentWeatherData_buf(self,buf,pos):
		self.logger.debug("")
		#CMinMaxMeasurement::CMinMaxMeasurement(&this->_PressureRelative_hPaMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_PressureRelative_inHgMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_WindSpeedMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_GustMinMax);
		#CMeasurement::CMeasurement(&thisa->_Rain1HMax);
		#CMeasurement::CMeasurement(&thisa->_Rain24HMax);
		#CMeasurement::CMeasurement(&thisa->_RainLastWeekMax);
		#CMeasurement::CMeasurement(&thisa->_RainLastMonthMax);
		self._LastRainReset = time.time()
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_IndoorTempMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_OutdoorTempMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_IndoorHumidityMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_OutdoorHumidityMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_DewpointMinMax);
		#CMinMaxMeasurement::CMinMaxMeasurement(&thisa->_WindchillMinMax);
		#std::bitset<29>::bitset<29>(&thisa->_AlarmRingingFlags);
		#std::bitset<29>::bitset<29>(&thisa->_AlarmMarkedFlags);
		self.read(buf,pos);

	def read(self,buf,pos):
		self.logger.debug("")
		newbuf = [0]
		newbuf[0] = buf[0]
		USBHardware.ReverseByteOrder(newbuf, pos + 0, 2);
		#CCurrentWeatherData::readAlarmFlags(thisa, buf, &thisa->_AlarmRingingFlags);
		self._WeatherState = newbuf[0][pos + 2] & 0xF;
		print "self._WeatherState", self._WeatherState

		self._WeatherTendency = (newbuf[0][pos + 2] >> 4) & 0xF;
		print "self._WeatherTendency",self._WeatherTendency

		#print "newbuf[0]",newbuf[0]
		USBHardware.ReverseByteOrder(newbuf, pos + 3, 0x12);
		#print "newbuf[0]",newbuf[0]
		#print "provatemp",newbuf[0][pos + 3]
		self._IndoorTemp = USBHardware.ToTemperature(newbuf, pos + 3, 1)
		print "self._IndoorTemp", self._IndoorTemp
		self.logger.debug("self._IndoorTemp=%d" % self._IndoorTemp)
		#  v3 = USBHardware::ToTemperature(buf[0], 5, 0);
		#  thisa->_IndoorTempMinMax._Min._Value = v3;
		#  v80 = thisa->_IndoorTempMinMax._Min._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_IndoorTempMinMax._Min._IsError = v80;
		#  v80 = thisa->_IndoorTempMinMax._Min._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_IndoorTempMinMax._Min._IsOverflow = v80;
		#  v4 = USBHardware::ToTemperature(buf + 8, 1);
		#  thisa->_IndoorTempMinMax._Max._Value = v4;
		#  v80 = thisa->_IndoorTempMinMax._Max._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_IndoorTempMinMax._Max._IsError = v80;
		#  v80 = thisa->_IndoorTempMinMax._Max._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_IndoorTempMinMax._Max._IsOverflow = v80;
		#if ( CMinMaxMeasurement::IsMinValueError(&thisa->_IndoorTempMinMax)
		#    || CMinMaxMeasurement::IsMinValueOverflow(&thisa->_IndoorTempMinMax) ):
		#    ATL::COleDateTime::SetStatus(&thisa->_IndoorTempMinMax._Min._Time, partial);
		#else:
		#    v5 = USBHardware::ToDateTime(&result, buf + 10, 0);
		#    v6 = (char *)&thisa->_IndoorTempMinMax._Min._Time;
		#    LODWORD(thisa->_IndoorTempMinMax._Min._Time.m_dt) = LODWORD(v5->m_dt);
		#    *((_DWORD *)v6 + 1) = HIDWORD(v5->m_dt);
		#    *((_DWORD *)v6 + 2) = v5->m_status;
		#if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_IndoorTempMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_IndoorTempMinMax) ):
		#    ATL::COleDateTime::SetStatus(&thisa->_IndoorTempMinMax._Max._Time, partial);
		#else:
		#    v7 = USBHardware::ToDateTime((ATL::COleDateTime *)&v82, buf + 15, 0);
		#    v8 = (char *)&thisa->_IndoorTempMinMax._Max._Time;
		#    LODWORD(thisa->_IndoorTempMinMax._Max._Time.m_dt) = LODWORD(v7->m_dt);
		#    *((_DWORD *)v8 + 1) = HIDWORD(v7->m_dt);
		#    *((_DWORD *)v8 + 2) = v7->m_status;
		USBHardware.ReverseByteOrder(newbuf, pos + 21, 0x12);
		self._OutdoorTemp = USBHardware.ToTemperature(newbuf, pos + 21, 1)
		print "self._OutdoorTemp", self._OutdoorTemp
		self.logger.debug("self._OutdoorTemp=%d" % self._OutdoorTemp)
		#  v10 = USBHardware::ToTemperature(buf + 23, 0);
		#  thisa->_OutdoorTempMinMax._Min._Value = v10;
		#  v80 = thisa->_OutdoorTempMinMax._Min._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_OutdoorTempMinMax._Min._IsError = v80;
		#  v80 = thisa->_OutdoorTempMinMax._Min._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_OutdoorTempMinMax._Min._IsOverflow = v80;
		#  v11 = USBHardware::ToTemperature(buf + 26, 1);
		#  thisa->_OutdoorTempMinMax._Max._Value = v11;
		#  v80 = thisa->_OutdoorTempMinMax._Max._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_OutdoorTempMinMax._Max._IsError = v80;
		#  v80 = thisa->_OutdoorTempMinMax._Max._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_OutdoorTempMinMax._Max._IsOverflow = v80;
		#  if ( CMinMaxMeasurement::IsMinValueError(&thisa->_OutdoorTempMinMax)
		#    || CMinMaxMeasurement::IsMinValueOverflow(&thisa->_OutdoorTempMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_OutdoorTempMinMax._Min._Time, partial);
		#  }
		#  else
		#  {
		#    v12 = USBHardware::ToDateTime((ATL::COleDateTime *)&v83, buf + 28, 0);
		#    v13 = (char *)&thisa->_OutdoorTempMinMax._Min._Time;
		#    LODWORD(thisa->_OutdoorTempMinMax._Min._Time.m_dt) = LODWORD(v12->m_dt);
		#    *((_DWORD *)v13 + 1) = HIDWORD(v12->m_dt);
		#    *((_DWORD *)v13 + 2) = v12->m_status;
		#  }
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_OutdoorTempMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_OutdoorTempMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_OutdoorTempMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v14 = USBHardware::ToDateTime((ATL::COleDateTime *)&v84, buf + 33, 0);
		#    v15 = (char *)&thisa->_OutdoorTempMinMax._Max._Time;
		#    LODWORD(thisa->_OutdoorTempMinMax._Max._Time.m_dt) = LODWORD(v14->m_dt);
		#    *((_DWORD *)v15 + 1) = HIDWORD(v14->m_dt);
		#    *((_DWORD *)v15 + 2) = v14->m_status;
		#  }
		#USBHardware.ReverseByteOrder(buf[0], 39, 0x12);
		#  v16 = USBHardware::ToTemperature(buf + 39, 1);
		#  thisa->_Windchill = v16;
		#  v17 = USBHardware::ToTemperature(buf + 41, 0);
		#  thisa->_WindchillMinMax._Min._Value = v17;
		#  v80 = thisa->_WindchillMinMax._Min._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_WindchillMinMax._Min._IsError = v80;
		#  v80 = thisa->_WindchillMinMax._Min._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_WindchillMinMax._Min._IsOverflow = v80;
		#  v18 = USBHardware::ToTemperature(buf + 44, 1);
		#  thisa->_WindchillMinMax._Max._Value = v18;
		#  v80 = thisa->_WindchillMinMax._Max._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_WindchillMinMax._Max._IsError = v80;
		#  v80 = thisa->_WindchillMinMax._Max._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_WindchillMinMax._Max._IsOverflow = v80;
		#  if ( CMinMaxMeasurement::IsMinValueError(&thisa->_WindchillMinMax)
		#    || CMinMaxMeasurement::IsMinValueOverflow(&thisa->_WindchillMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_WindchillMinMax._Min._Time, partial);
		#  }
		#  else
		#  {
		#    v19 = USBHardware::ToDateTime((ATL::COleDateTime *)&v85, buf + 46, 0);
		#    v20 = (char *)&thisa->_WindchillMinMax._Min._Time;
		#    LODWORD(thisa->_WindchillMinMax._Min._Time.m_dt) = LODWORD(v19->m_dt);
		#    *((_DWORD *)v20 + 1) = HIDWORD(v19->m_dt);
		#    *((_DWORD *)v20 + 2) = v19->m_status;
		#  }
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_WindchillMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_WindchillMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_WindchillMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v21 = USBHardware::ToDateTime((ATL::COleDateTime *)&v86, buf + 51, 0);
		#    v22 = (char *)&thisa->_WindchillMinMax._Max._Time;
		#    LODWORD(thisa->_WindchillMinMax._Max._Time.m_dt) = LODWORD(v21->m_dt);
		#    *((_DWORD *)v22 + 1) = HIDWORD(v21->m_dt);
		#    *((_DWORD *)v22 + 2) = v21->m_status;
		#  }
		#  USBHardware::ReverseByteOrder(buf[0], 57, 0x12);
		#  v23 = USBHardware::ToTemperature(buf + 57, 1);
		#  thisa->_Dewpoint = v23;
		#  v24 = USBHardware::ToTemperature(buf + 59, 0);
		#  thisa->_DewpointMinMax._Min._Value = v24;
		#  v80 = thisa->_DewpointMinMax._Min._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_DewpointMinMax._Min._IsError = v80;
		#  v80 = thisa->_DewpointMinMax._Min._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_DewpointMinMax._Min._IsOverflow = v80;
		#  v25 = USBHardware::ToTemperature(buf + 62, 1);
		#  thisa->_DewpointMinMax._Max._Value = v25;
		#  v80 = thisa->_DewpointMinMax._Max._Value == CWeatherTraits::TemperatureNP();
		#  thisa->_DewpointMinMax._Max._IsError = v80;
		#  v80 = thisa->_DewpointMinMax._Max._Value == CWeatherTraits::TemperatureOFL();
		#  thisa->_DewpointMinMax._Max._IsOverflow = v80;
		#  if ( CMinMaxMeasurement::IsMinValueError(&thisa->_DewpointMinMax)
		#    || CMinMaxMeasurement::IsMinValueOverflow(&thisa->_DewpointMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_DewpointMinMax._Min._Time, partial);
		#  }
		#  else
		#  {
		#    v26 = USBHardware::ToDateTime((ATL::COleDateTime *)&v87, buf + 64, 0);
		#    v27 = (char *)&thisa->_DewpointMinMax._Min._Time;
		#    LODWORD(thisa->_DewpointMinMax._Min._Time.m_dt) = LODWORD(v26->m_dt);
		#    *((_DWORD *)v27 + 1) = HIDWORD(v26->m_dt);
		#    *((_DWORD *)v27 + 2) = v26->m_status;
		#  }
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_DewpointMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_DewpointMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_DewpointMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v28 = USBHardware::ToDateTime((ATL::COleDateTime *)&v88, buf + 69, 0);
		#    v29 = (char *)&thisa->_DewpointMinMax._Max._Time;
		#    LODWORD(thisa->_DewpointMinMax._Max._Time.m_dt) = LODWORD(v28->m_dt);
		#    *((_DWORD *)v29 + 1) = HIDWORD(v28->m_dt);
		#    *((_DWORD *)v29 + 2) = v28->m_status;
		#  }

		USBHardware.ReverseByteOrder(newbuf, pos + 75, 0xD);
		v30 = USBHardware.ToHumidity(buf, pos + 75, 1);
		self._IndoorHumidity = v30;
		print "self._IndoorHumidity", self._IndoorHumidity
		self.logger.debug("self._IndoorHumidity=%d" % self._IndoorHumidity)

		#  v31 = USBHardware::ToHumidity(buf + 76, 1);
		#  thisa->_IndoorHumidityMinMax._Min._Value = v31;
		#  v80 = thisa->_IndoorHumidityMinMax._Min._Value == CWeatherTraits::HumidityNP();
		#  thisa->_IndoorHumidityMinMax._Min._IsError = v80;
		#  v80 = thisa->_IndoorHumidityMinMax._Min._Value == CWeatherTraits::HumidityOFL();
		#  thisa->_IndoorHumidityMinMax._Min._IsOverflow = v80;
		#  v32 = USBHardware::ToHumidity(buf + 77, 1);
		#  thisa->_IndoorHumidityMinMax._Max._Value = v32;
		#  v80 = thisa->_IndoorHumidityMinMax._Max._Value == CWeatherTraits::HumidityNP();
		#  thisa->_IndoorHumidityMinMax._Max._IsError = v80;
		#  v80 = thisa->_IndoorHumidityMinMax._Max._Value == CWeatherTraits::HumidityOFL();
		#  thisa->_IndoorHumidityMinMax._Max._IsOverflow = v80;
		#  if ( CMinMaxMeasurement::IsMinValueError(&thisa->_IndoorHumidityMinMax)
		#    || CMinMaxMeasurement::IsMinValueOverflow(&thisa->_IndoorHumidityMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_IndoorHumidityMinMax._Min._Time, partial);
		#  }
		#  else
		#  {
		#    v33 = USBHardware::ToDateTime((ATL::COleDateTime *)&v89, buf + 78, 1);
		#    v34 = (char *)&thisa->_IndoorHumidityMinMax._Min._Time;
		#    LODWORD(thisa->_IndoorHumidityMinMax._Min._Time.m_dt) = LODWORD(v33->m_dt);
		#    *((_DWORD *)v34 + 1) = HIDWORD(v33->m_dt);
		#    *((_DWORD *)v34 + 2) = v33->m_status;
		#  }
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_IndoorHumidityMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_IndoorHumidityMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_IndoorHumidityMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v35 = USBHardware::ToDateTime((ATL::COleDateTime *)&v90, buf + 83, 1);
		#    v36 = (char *)&thisa->_IndoorHumidityMinMax._Max._Time;
		#    LODWORD(thisa->_IndoorHumidityMinMax._Max._Time.m_dt) = LODWORD(v35->m_dt);
		#    *((_DWORD *)v36 + 1) = HIDWORD(v35->m_dt);
		#    *((_DWORD *)v36 + 2) = v35->m_status;
		#  }

		USBHardware.ReverseByteOrder(newbuf, pos + 88, 0xD);
		v37 = USBHardware.ToHumidity(buf,pos + 88, 1);
		self._OutdoorHumidity = v37;
		print "self._OutdoorHumidity", self._OutdoorHumidity
		self.logger.debug("self._OutdoorHumidity=%d" % self._OutdoorHumidity)

		#  v38 = USBHardware::ToHumidity(buf + 89, 1);
		#  thisa->_OutdoorHumidityMinMax._Min._Value = v38;
		#  v80 = thisa->_OutdoorHumidityMinMax._Min._Value == CWeatherTraits::HumidityNP();
		#  thisa->_OutdoorHumidityMinMax._Min._IsError = v80;
		#  v80 = thisa->_OutdoorHumidityMinMax._Min._Value == CWeatherTraits::HumidityOFL();
		#  thisa->_OutdoorHumidityMinMax._Min._IsOverflow = v80;
		#  v39 = USBHardware::ToHumidity(buf + 90, 1);
		#  thisa->_OutdoorHumidityMinMax._Max._Value = v39;
		#  v80 = thisa->_OutdoorHumidityMinMax._Max._Value == CWeatherTraits::HumidityNP();
		#  thisa->_OutdoorHumidityMinMax._Max._IsError = v80;
		#  v80 = thisa->_OutdoorHumidityMinMax._Max._Value == CWeatherTraits::HumidityOFL();
		#  thisa->_OutdoorHumidityMinMax._Max._IsOverflow = v80;
		#  if ( CMinMaxMeasurement::IsMinValueError(&thisa->_OutdoorHumidityMinMax)
		#    || CMinMaxMeasurement::IsMinValueOverflow(&thisa->_OutdoorHumidityMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_OutdoorHumidityMinMax._Min._Time, partial);
		#  }
		#  else
		#  {
		#    v40 = USBHardware::ToDateTime((ATL::COleDateTime *)&v91, buf + 91, 1);
		#    v41 = (char *)&thisa->_OutdoorHumidityMinMax._Min._Time;
		#    LODWORD(thisa->_OutdoorHumidityMinMax._Min._Time.m_dt) = LODWORD(v40->m_dt);
		#    *((_DWORD *)v41 + 1) = HIDWORD(v40->m_dt);
		#    *((_DWORD *)v41 + 2) = v40->m_status;
		#  }
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_OutdoorHumidityMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_OutdoorHumidityMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_OutdoorHumidityMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v42 = USBHardware::ToDateTime((ATL::COleDateTime *)&v92, buf + 96, 1);
		#    v43 = (char *)&thisa->_OutdoorHumidityMinMax._Max._Time;
		#    LODWORD(thisa->_OutdoorHumidityMinMax._Max._Time.m_dt) = LODWORD(v42->m_dt);
		#    *((_DWORD *)v43 + 1) = HIDWORD(v42->m_dt);
		#    *((_DWORD *)v43 + 2) = v42->m_status;
		#  }
		#  USBHardware::ReverseByteOrder(buf + 101, 0xBu);
		#  v44 = USBHardware::To4Pre2Post(buf + 101);
		#  thisa->_RainLastMonth = v44;
		#  v45 = USBHardware::To4Pre2Post(buf + 104);
		#  thisa->_RainLastMonthMax._Value = v45;
		#  v80 = thisa->_RainLastMonthMax._Value == CWeatherTraits::RainNP();
		#  thisa->_RainLastMonthMax._IsError = v80;
		#  v80 = thisa->_RainLastMonthMax._Value == CWeatherTraits::RainOFL();
		#  thisa->_RainLastMonthMax._IsOverflow = v80;
		#  if ( CMeasurement::IsError(&thisa->_RainLastMonthMax) || CMeasurement::IsOverflow(&thisa->_RainLastMonthMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_RainLastMonthMax._Time, partial);
		#  }
		#  else
		#  {
		#    v46 = USBHardware::ToDateTime((ATL::COleDateTime *)&v93, buf + 107, 1);
		#    v47 = (char *)&thisa->_RainLastMonthMax._Time;
		#    LODWORD(thisa->_RainLastMonthMax._Time.m_dt) = LODWORD(v46->m_dt);
		#    *((_DWORD *)v47 + 1) = HIDWORD(v46->m_dt);
		#    *((_DWORD *)v47 + 2) = v46->m_status;
		#  }
		#  USBHardware::ReverseByteOrder(buf + 112, 0xBu);
		#  v48 = USBHardware::To4Pre2Post(buf + 112);
		#  thisa->_RainLastWeek = v48;
		#  v49 = USBHardware::To4Pre2Post(buf + 115);
		#  thisa->_RainLastWeekMax._Value = v49;
		#  v80 = thisa->_RainLastWeekMax._Value == CWeatherTraits::RainNP();
		#  thisa->_RainLastWeekMax._IsError = v80;
		#  v80 = thisa->_RainLastWeekMax._Value == CWeatherTraits::RainOFL();
		#  thisa->_RainLastWeekMax._IsOverflow = v80;
		#  if ( CMeasurement::IsError(&thisa->_RainLastWeekMax) || CMeasurement::IsOverflow(&thisa->_RainLastWeekMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_RainLastWeekMax._Time, partial);
		#  }
		#  else
		#  {
		#    v50 = USBHardware::ToDateTime((ATL::COleDateTime *)&v94, buf + 118, 1);
		#    v51 = (char *)&thisa->_RainLastWeekMax._Time;
		#    LODWORD(thisa->_RainLastWeekMax._Time.m_dt) = LODWORD(v50->m_dt);
		#    *((_DWORD *)v51 + 1) = HIDWORD(v50->m_dt);
		#    *((_DWORD *)v51 + 2) = v50->m_status;
		#  }
		#  USBHardware::ReverseByteOrder(buf + 123, 0xBu);
		#  v52 = USBHardware::To4Pre2Post(buf + 123);
		#  thisa->_Rain24H = v52;
		#  v53 = USBHardware::To4Pre2Post(buf + 126);
		#  thisa->_Rain24HMax._Value = v53;
		#  v80 = thisa->_Rain24HMax._Value == CWeatherTraits::RainNP();
		#  thisa->_Rain24HMax._IsError = v80;
		#  v80 = thisa->_Rain24HMax._Value == CWeatherTraits::RainOFL();
		#  thisa->_Rain24HMax._IsOverflow = v80;
		#  if ( CMeasurement::IsError(&thisa->_Rain24HMax) || CMeasurement::IsOverflow(&thisa->_Rain24HMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_Rain24HMax._Time, partial);
		#  }
		#  else
		#  {
		#    v54 = USBHardware::ToDateTime((ATL::COleDateTime *)&v95, buf + 129, 1);
		#    v55 = (char *)&thisa->_Rain24HMax._Time;
		#    LODWORD(thisa->_Rain24HMax._Time.m_dt) = LODWORD(v54->m_dt);
		#    *((_DWORD *)v55 + 1) = HIDWORD(v54->m_dt);
		#    *((_DWORD *)v55 + 2) = v54->m_status;
		#  }
		#  USBHardware::ReverseByteOrder(buf + 134, 0xBu);
		#  v56 = USBHardware::To4Pre2Post(buf + 134);
		#  thisa->_Rain1H = v56;
		#  v57 = USBHardware::To4Pre2Post(buf + 137);
		#  thisa->_Rain1HMax._Value = v57;
		#  v80 = thisa->_Rain1HMax._Value == CWeatherTraits::RainNP();
		#  thisa->_Rain1HMax._IsError = v80;
		#  v80 = thisa->_Rain1HMax._Value == CWeatherTraits::RainOFL();
		#  thisa->_Rain1HMax._IsOverflow = v80;
		#  if ( CMeasurement::IsError(&thisa->_Rain1HMax) || CMeasurement::IsOverflow(&thisa->_Rain1HMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_Rain1HMax._Time, partial);
		#  }
		#  else
		#  {
		#    v58 = USBHardware::ToDateTime((ATL::COleDateTime *)&v96, buf + 140, 1);
		#    v59 = (char *)&thisa->_Rain1HMax._Time;
		#    LODWORD(thisa->_Rain1HMax._Time.m_dt) = LODWORD(v58->m_dt);
		#    *((_DWORD *)v59 + 1) = HIDWORD(v58->m_dt);
		#    *((_DWORD *)v59 + 2) = v58->m_status;
		#  }
		#  USBHardware::ReverseByteOrder(buf + 145, 9u);
		#  v60 = USBHardware::To4Pre3Post(buf + 145);
		#  thisa->_RainTotal = v60;
		#  v61 = USBHardware::ToDateTime((ATL::COleDateTime *)&v97, buf + 148, 0);
		#  v62 = (char *)&thisa->_LastRainReset;
		#  LODWORD(thisa->_LastRainReset.m_dt) = LODWORD(v61->m_dt);
		#  *((_DWORD *)v62 + 1) = HIDWORD(v61->m_dt);
		#  *((_DWORD *)v62 + 2) = v61->m_status;
		#  USBHardware::ReverseByteOrder(buf + 154, 0xFu);
		#  v63 = USBHardware::ToWindspeed(buf + 154);
		#  thisa->_WindSpeed = v63;
		#  v64 = USBHardware::ToWindspeed(buf + 157);
		#  thisa->_WindSpeedMinMax._Max._Value = v64;
		#  v80 = thisa->_WindSpeedMinMax._Min._Value == CWeatherTraits::WindNP();
		#  thisa->_WindSpeedMinMax._Max._IsError = v80;
		#  v80 = thisa->_WindSpeedMinMax._Min._Value == CWeatherTraits::WindOFL();
		#  thisa->_WindSpeedMinMax._Max._IsOverflow = v80;
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_WindSpeedMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_WindSpeedMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_WindSpeedMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v65 = USBHardware::ToDateTime((ATL::COleDateTime *)&v98, buf + 160, 1);
		#    v66 = (char *)&thisa->_WindSpeedMinMax._Max._Time;
		#    LODWORD(thisa->_WindSpeedMinMax._Max._Time.m_dt) = LODWORD(v65->m_dt);
		#    *((_DWORD *)v66 + 1) = HIDWORD(v65->m_dt);
		#    *((_DWORD *)v66 + 2) = v65->m_status;
		#  }
		#  WindErrFlags = buf[165];
		#  USBHardware::ReadWindDirectionShared(buf + 166, (int *)&w, (int *)&w1);
		#  USBHardware::ReadWindDirectionShared(buf + 167, (int *)&w2, (int *)&w3);
		#  USBHardware::ReadWindDirectionShared(buf + 168, (int *)&w4, (int *)&w5);
		#  thisa->_WindDirection = w;
		#  thisa->_WindDirection1 = w1;
		#  thisa->_WindDirection2 = w2;
		#  thisa->_WindDirection3 = w3;
		#  thisa->_WindDirection4 = w4;
		#  thisa->_WindDirection5 = w5;
		#  CCurrentWeatherData::CheckWindErrFlags(
		#    thisa,
		#    WindErrFlags,
		#    &thisa->_WindSpeed,
		#    &thisa->_WindSpeedMinMax,
		#    &thisa->_WindDirection,
		#    &thisa->_WindDirection1,
		#    &thisa->_WindDirection2,
		#    &thisa->_WindDirection3,
		#    &thisa->_WindDirection4,
		#    &thisa->_WindDirection5);
		#  USBHardware::ReverseByteOrder(buf + 169, 0xFu);
		#  v67 = USBHardware::ToWindspeed(buf + 169);
		#  thisa->_Gust = v67;
		#  v68 = USBHardware::ToWindspeed(buf + 172);
		#  thisa->_GustMinMax._Max._Value = v68;
		#  v80 = thisa->_GustMinMax._Min._Value == CWeatherTraits::WindNP();
		#  thisa->_GustMinMax._Max._IsError = v80;
		#  v80 = thisa->_GustMinMax._Min._Value == CWeatherTraits::WindOFL();
		#  thisa->_GustMinMax._Max._IsOverflow = v80;
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_GustMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_GustMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_GustMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v69 = USBHardware::ToDateTime((ATL::COleDateTime *)&v99, buf + 175, 1);
		#    v70 = (char *)&thisa->_GustMinMax._Max._Time;
		#    LODWORD(thisa->_GustMinMax._Max._Time.m_dt) = LODWORD(v69->m_dt);
		#    *((_DWORD *)v70 + 1) = HIDWORD(v69->m_dt);
		#    *((_DWORD *)v70 + 2) = v69->m_status;
		#  }
		#  GustErrFlags = buf[180];
		#  USBHardware::ReadWindDirectionShared(buf + 181, (int *)&g, (int *)&g1);
		#  USBHardware::ReadWindDirectionShared(buf + 182, (int *)&g2, (int *)&g3);
		#  USBHardware::ReadWindDirectionShared(buf + 183, (int *)&g4, (int *)&g5);
		#  thisa->_GustDirection = g;
		#  thisa->_GustDirection1 = g1;
		#  thisa->_GustDirection2 = g2;
		#  thisa->_GustDirection3 = g3;
		#  thisa->_GustDirection4 = g4;
		#  thisa->_GustDirection5 = g5;
		#  CCurrentWeatherData::CheckWindErrFlags(
		#    thisa,
		#    GustErrFlags,
		#    &thisa->_Gust,
		#    &thisa->_GustMinMax,
		#    &thisa->_GustDirection,
		#    &thisa->_GustDirection1,
		#    &thisa->_GustDirection2,
		#    &thisa->_GustDirection3,
		#    &thisa->_GustDirection4,
		#    &thisa->_GustDirection5);
		#  USBHardware::ReverseByteOrder(buf + 184, 0x19u);
		#  USBHardware::ReadPressureShared(buf + 184, &thisa->_PressureRelative_hPa, &thisa->_PressureRelative_inHg);
		#  USBHardware::ReadPressureShared(buf + 189, &min_hPa, &min_inHg);
		#  USBHardware::ReadPressureShared(buf + 194, &max_hPa, &max_inHg);
		#  thisa->_PressureRelative_hPaMinMax._Min._Value = CWeatherTraits::PressureOFL();
		#  thisa->_PressureRelative_hPaMinMax._Min._IsError = 1;
		#  thisa->_PressureRelative_hPaMinMax._Min._IsOverflow = 1;
		#  thisa->_PressureRelative_hPaMinMax._Max._Value = CWeatherTraits::PressureOFL();
		#  thisa->_PressureRelative_hPaMinMax._Max._IsError = 1;
		#  thisa->_PressureRelative_hPaMinMax._Max._IsOverflow = 1;
		#  if ( CMinMaxMeasurement::IsMinValueError(&thisa->_PressureRelative_hPaMinMax)
		#    || CMinMaxMeasurement::IsMinValueOverflow(&thisa->_PressureRelative_hPaMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_PressureRelative_hPaMinMax._Min._Time, partial);
		#    ATL::COleDateTime::SetStatus(&thisa->_PressureRelative_inHgMinMax._Min._Time, partial);
		#  }
		#  else
		#  {
		#    v71 = USBHardware::ToDateTime((ATL::COleDateTime *)&v100, buf + 199, 1);
		#    v72 = (char *)&thisa->_PressureRelative_hPaMinMax._Min._Time;
		#    LODWORD(thisa->_PressureRelative_hPaMinMax._Min._Time.m_dt) = LODWORD(v71->m_dt);
		#    *((_DWORD *)v72 + 1) = HIDWORD(v71->m_dt);
		#    *((_DWORD *)v72 + 2) = v71->m_status;
		#    v73 = (char *)&thisa->_PressureRelative_hPaMinMax._Min._Time;
		#    v74 = (char *)&thisa->_PressureRelative_inHgMinMax._Min._Time;
		#    LODWORD(thisa->_PressureRelative_inHgMinMax._Min._Time.m_dt) = LODWORD(thisa->_PressureRelative_hPaMinMax._Min._Time.m_dt);
		#    *((_DWORD *)v74 + 1) = *((_DWORD *)v73 + 1);
		#    *((_DWORD *)v74 + 2) = *((_DWORD *)v73 + 2);
		#  }
		#  if ( CMinMaxMeasurement::IsMaxValueError(&thisa->_PressureRelative_hPaMinMax)
		#    || CMinMaxMeasurement::IsMaxValueOverflow(&thisa->_PressureRelative_hPaMinMax) )
		#  {
		#    ATL::COleDateTime::SetStatus(&thisa->_PressureRelative_hPaMinMax._Max._Time, partial);
		#    ATL::COleDateTime::SetStatus(&thisa->_PressureRelative_inHgMinMax._Max._Time, partial);
		#  }
		#  else
		#  {
		#    v75 = USBHardware::ToDateTime((ATL::COleDateTime *)&v101, buf + 204, 1);
		#    v76 = (char *)&thisa->_PressureRelative_hPaMinMax._Max._Time;
		#    LODWORD(thisa->_PressureRelative_hPaMinMax._Max._Time.m_dt) = LODWORD(v75->m_dt);
		#    *((_DWORD *)v76 + 1) = HIDWORD(v75->m_dt);
		#    *((_DWORD *)v76 + 2) = v75->m_status;
		#    v77 = (char *)&thisa->_PressureRelative_hPaMinMax._Max._Time;
		#    v78 = (char *)&thisa->_PressureRelative_inHgMinMax._Max._Time;
		#    LODWORD(thisa->_PressureRelative_inHgMinMax._Max._Time.m_dt) = LODWORD(thisa->_PressureRelative_hPaMinMax._Max._Time.m_dt);
		#    *((_DWORD *)v78 + 1) = *((_DWORD *)v77 + 1);
		#    *((_DWORD *)v78 + 2) = *((_DWORD *)v77 + 2);
		#  }
		#  thisa->_PressureRelative_inHgMinMax._Min._Value = CWeatherTraits::PressureOFL();
		#  thisa->_PressureRelative_inHgMinMax._Min._IsError = 1;
		#  thisa->_PressureRelative_inHgMinMax._Min._IsOverflow = 1;
		#  thisa->_PressureRelative_inHgMinMax._Max._Value = CWeatherTraits::PressureOFL();
		#  thisa->_PressureRelative_inHgMinMax._Max._IsError = 1;
		#  thisa->_PressureRelative_inHgMinMax._Max._IsOverflow = 1;
		#  std::bitset<29>::bitset<29>((std::bitset<29> *)&v102, 0);
		#  thisa->_AlarmMarkedFlags._Array[0] = v102;
