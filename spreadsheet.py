#!/usr/bin/python


# For parsing config files.
from ConfigParser import SafeConfigParser

# For working with the operating system.
import os 

# For working with google spreadsheets.
import gspread


class Spreadsheet:
    """
    A very simple helper class that logs in
    and loads a spreadsheet in your google docs.

    """

    @staticmethod
    def load(spreadsheet):
        """
        Loads a spreadsheet.

        """

        # What is the name of the settings file?
        settings_file = "settings"

        # Does it exist in this folder?
        try:
            open(settings_file)
        except IOError:
            print "No settings file in your current folder."
            print "Are you in the right folder?"
            return

        # Instantiate a config parser.
        parser = SafeConfigParser()

        # Read the settings file.
        parser.read(settings_file)

        # Is there a 'credentials' setting?
        if parser.has_section('credentials'):

            # Is there a username?
            username = parser.get('credentials', 'username')
            if username is None:
                print "No username in the settings file."
                return

            # Is there a password?
            password = parser.get('credentials', 'password')
            if password is None:
                print "No password in the settings file."
                return

            # Now log in.
            gspread_connection = gspread.login(username, password)

            # Open the worksheet.
            worksheet = gspread_connection.open(spreadsheet).sheet1

            # Return it.
            return worksheet            

        # If no credentials in the settings file, report it.
        else:
            print "No credentials in the settings file."
            return

