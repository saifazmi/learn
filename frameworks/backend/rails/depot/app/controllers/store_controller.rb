# frozen_string_literal: true

# Root controller for the application
class StoreController < ApplicationController
  def index
    @products = Product.order(:title)
  end
end
